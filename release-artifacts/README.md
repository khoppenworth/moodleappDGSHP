# Release artifacts

## `dgshp-elearning-identity-test.apk`

This repository no longer checks in the generated APK binary because binary artifacts can block pull request creation/review.

You can still generate a **debug-signed identity smoke-test APK** locally with `scripts/create-identity-test-apk.py`. The generated file is intentionally minimal and is **not** the production Moodle App build. It is useful only for quick Android package/display-name checks:

- Package ID: `org.santegovml.elearning`
- Display name: `DGSHP e-Learning`
- Version name: `5.2.0-test`
- Version code: `52001`
- Signature: debug/self-signed

Do not upload the generated identity APK to Google Play and do not distribute it as the final app. Generate the real Moodle App debug APK or signed release AAB using the build instructions in `docs/DGSHP_BRANDING.md` once Node 22, npm dependencies, Android SDK tooling, and signing credentials are available.

To generate this local artifact:

```bash
python scripts/create-identity-test-apk.py
jarsigner -verify -certs release-artifacts/dgshp-elearning-identity-test.apk
```

The APK filename is ignored by Git so you can generate and download/use it locally without adding the binary to a pull request.
