#!/usr/bin/env python3
"""Create the local DGSHP e-Learning identity smoke-test APK.

This script intentionally does not build the full Moodle App. It creates a
minimal debug-signed APK with the DGSHP package id and display name so release
reviewers can verify Android identity metadata when a full Cordova/Android SDK
build environment is unavailable.
"""
import pathlib, shutil, struct, subprocess, zipfile

OUT = pathlib.Path('release-artifacts/dgshp-elearning-identity-test.apk')
TMP = pathlib.Path('/tmp/dgshp-apk/build')
PACKAGE = 'org.santegovml.elearning'
LABEL = 'DGSHP e-Learning'
VERSION_NAME = '5.2.0-test'
VERSION_CODE = 52001

# Android binary XML constants.
RES_STRING_POOL_TYPE = 0x0001
RES_XML_TYPE = 0x0003
RES_XML_RESOURCE_MAP_TYPE = 0x0180
RES_XML_START_NAMESPACE_TYPE = 0x0100
RES_XML_END_NAMESPACE_TYPE = 0x0101
RES_XML_START_ELEMENT_TYPE = 0x0102
RES_XML_END_ELEMENT_TYPE = 0x0103
UTF8_FLAG = 0x00000100
NO_INDEX = 0xFFFFFFFF
ANDROID_NS = 'http://schemas.android.com/apk/res/android'

strings = []
def sid(s):
    if s not in strings:
        strings.append(s)
    return strings.index(s)

# Pre-register strings in the order the resource map expects for framework attrs.
for s in [
    'manifest', ANDROID_NS, 'android', 'package', 'versionCode', 'versionName',
    'uses-sdk', 'minSdkVersion', 'targetSdkVersion', 'application', 'label',
    'allowBackup', 'activity', 'name', 'exported', 'intent-filter', 'action',
    'category', PACKAGE, VERSION_NAME, '24', '36', LABEL, 'false',
    'android.app.Activity', 'true', 'android.intent.action.MAIN',
    'android.intent.category.LAUNCHER'
]:
    sid(s)

RESOURCE_IDS = {
    'package': 0x01010003,
    'versionCode': 0x0101021b,
    'versionName': 0x0101021c,
    'minSdkVersion': 0x0101020c,
    'targetSdkVersion': 0x01010270,
    'label': 0x01010001,
    'allowBackup': 0x01010280,
    'name': 0x01010003,
    'exported': 0x01010010,
}

def u8len(n):
    if n > 0x7f:
        return bytes([(n >> 8) | 0x80, n & 0xff])
    return bytes([n])

def align4(b):
    return b + b'\x00' * ((4 - len(b) % 4) % 4)

def chunk(t, header_size, body):
    return struct.pack('<HHI', t, header_size, header_size + len(body)) + body

def string_pool():
    encoded = []
    offsets = []
    data = b''
    for s in strings:
        raw = s.encode('utf-8')
        offsets.append(len(data))
        data += u8len(len(s)) + u8len(len(raw)) + raw + b'\x00'
    data = align4(data)
    string_count = len(strings)
    header_size = 28
    strings_start = header_size + 4 * string_count
    body = struct.pack('<IIIII', string_count, 0, UTF8_FLAG, strings_start, 0)
    body += b''.join(struct.pack('<I', o) for o in offsets)
    body += data
    return chunk(RES_STRING_POOL_TYPE, header_size, body)

def resource_map():
    ids = []
    for s in strings:
        ids.append(RESOURCE_IDS.get(s, 0))
    # Android accepts a sparse resource map; zeroes are harmless for non-attr strings.
    return chunk(RES_XML_RESOURCE_MAP_TYPE, 8, b''.join(struct.pack('<I', i) for i in ids))

def node_header(t, body_size, line=1):
    return struct.pack('<HHIII', t, 16, 16 + body_size, line, NO_INDEX)

def start_ns():
    body = struct.pack('<II', sid('android'), sid(ANDROID_NS))
    return node_header(RES_XML_START_NAMESPACE_TYPE, len(body)) + body

def end_ns():
    body = struct.pack('<II', sid('android'), sid(ANDROID_NS))
    return node_header(RES_XML_END_NAMESPACE_TYPE, len(body)) + body

def typed_string(value):
    return sid(value), 8, 0, 0x03, sid(value)

def typed_int(value):
    return NO_INDEX, 8, 0, 0x10, value

def typed_bool(value):
    return NO_INDEX, 8, 0, 0x12, 0xFFFFFFFF if value else 0

def attr(name, value, ns=True):
    if isinstance(value, bool):
        raw, size, res0, typ, data = typed_bool(value)
    elif isinstance(value, int):
        raw, size, res0, typ, data = typed_int(value)
    else:
        raw, size, res0, typ, data = typed_string(value)
    return struct.pack('<IIIHBBI', sid(ANDROID_NS) if ns else NO_INDEX, sid(name), raw, size, res0, typ, data)

def start_el(name, attrs):
    attrs = sorted(attrs, key=lambda a: (a[0], a[1]))
    attr_bytes = b''.join(attr(*a) for a in attrs)
    ext = struct.pack('<IIHHHHHH', NO_INDEX, sid(name), 20, 20, len(attrs), 0, 0, 0)
    return node_header(RES_XML_START_ELEMENT_TYPE, len(ext) + len(attr_bytes)) + ext + attr_bytes

def end_el(name):
    body = struct.pack('<II', NO_INDEX, sid(name))
    return node_header(RES_XML_END_ELEMENT_TYPE, len(body)) + body

def manifest_axml():
    xml_body = b''
    xml_body += string_pool()
    xml_body += resource_map()
    xml_body += start_ns()
    xml_body += start_el('manifest', [
        ('package', PACKAGE, False),
        ('versionCode', VERSION_CODE, True),
        ('versionName', VERSION_NAME, True),
    ])
    xml_body += start_el('uses-sdk', [
        ('minSdkVersion', 24, True),
        ('targetSdkVersion', 36, True),
    ])
    xml_body += end_el('uses-sdk')
    xml_body += start_el('application', [
        ('label', LABEL, True),
        ('allowBackup', False, True),
    ])
    xml_body += start_el('activity', [
        ('name', 'android.app.Activity', True),
        ('exported', True, True),
        ('label', LABEL, True),
    ])
    xml_body += start_el('intent-filter', [])
    xml_body += start_el('action', [('name', 'android.intent.action.MAIN', True)])
    xml_body += end_el('action')
    xml_body += start_el('category', [('name', 'android.intent.category.LAUNCHER', True)])
    xml_body += end_el('category')
    xml_body += end_el('intent-filter')
    xml_body += end_el('activity')
    xml_body += end_el('application')
    xml_body += end_el('manifest')
    xml_body += end_ns()
    return chunk(RES_XML_TYPE, 8, xml_body)

def main():
    if TMP.exists():
        shutil.rmtree(TMP)
    TMP.mkdir(parents=True)
    unsigned = TMP / 'unsigned.apk'
    with zipfile.ZipFile(unsigned, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('AndroidManifest.xml', manifest_axml())
    keystore = TMP / 'debug.keystore'
    subprocess.run([
        'keytool', '-genkeypair', '-keystore', str(keystore), '-storepass', 'android',
        '-keypass', 'android', '-alias', 'androiddebugkey', '-keyalg', 'RSA',
        '-keysize', '2048', '-validity', '10000', '-dname', 'CN=Android Debug,O=DGSHP,C=ML'
    ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    signed = TMP / 'signed.apk'
    shutil.copyfile(unsigned, signed)
    subprocess.run([
        'jarsigner', '-keystore', str(keystore), '-storepass', 'android', '-keypass', 'android',
        '-signedjar', str(OUT), str(signed), 'androiddebugkey'
    ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(OUT)

if __name__ == '__main__':
    main()
