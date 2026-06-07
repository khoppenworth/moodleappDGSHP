# DGSHP e-Learning Moodle App Customization

This fork customizes the existing Moodle App for the **Direction Générale de la Santé et de l'Hygiène Publique, Mali**. It does not create a new app from scratch and does not convert Moodle App into a webview-only wrapper.

## Summary of changes

- App display name: **DGSHP e-Learning**
- Android package ID: `org.santegovml.elearning`
- iOS bundle ID: `org.santegovml.elearning`
- Primary language: French (`fr`)
- Secondary language: English (`en`)
- Target Moodle site: `https://e-learning.santegovml.org/`
- Branding palette: public-health green/blue with a light mint background
- Branding asset replacement locations documented; binary placeholder images are intentionally not changed in this PR to avoid binary-file review/PR creation issues

## Files changed for identity and configuration

| Area | Files |
| --- | --- |
| Native Cordova identity | `config.xml` |
| Runtime Moodle App configuration | `moodle.config.json` |
| Package/project metadata | `package.json`, `package-lock.json`, `ionic.config.json` |
| Android Firebase placeholder package | `google-services.json` |
| iOS Firebase placeholder bundle | `GoogleService-Info.plist` |
| Theme variables/styles | `src/theme/globals.custom.scss`, `src/theme/theme.custom.scss` |
| App and splash assets | `resources/icon.png`, `resources/splash.png`, `resources/android/icon-foreground.png`, `resources/android/android-splash.xml`, `resources/values/colors.xml` |
| Notification icon assets | `resources/android/icon/drawable-*-smallicon.png` |
| Web/login assets | `src/assets/icon/icon.png`, `src/assets/icon/favicon.png`, `src/assets/img/login_logo.png`, `src/assets/img/top_logo.png` |
| Documentation | `docs/DGSHP_BRANDING.md`, `docs/STORE_READINESS.md`, `docs/RELEASE_QA_CHECKLIST.md` |

## Moodle site preconfiguration

The app is preconfigured in `moodle.config.json` using the Moodle App `sites` configuration:

```json
"sites": [
    {
        "name": "DGSHP e-Learning",
        "url": "https://e-learning.santegovml.org/"
    }
]
```

This Moodle App version routes directly to the credentials page when exactly one fixed site is configured. Users should not need to type the Moodle site URL on first use.

`onlyallowlistedsites` is set to `true` so logins are restricted to the configured DGSHP Moodle site.

## Changing the Moodle site URL later

To change the Moodle site URL:

1. Edit `moodle.config.json`.
2. Update the `sites[0].url` value.
3. If the display name should change, update `sites[0].name`.
4. Rebuild the app so the generated `src/assets/env.json` contains the new configuration.
5. QA login, SSO, deep links, notifications, and offline sync against the new Moodle site.

If multiple Moodle sites should be available, add multiple entries to `sites` and review `multisitesdisplay`, `sitefindersettings`, and `onlyallowlistedsites`.

## Replacing placeholder branding assets

Binary image assets are intentionally not changed in this PR to avoid binary-file review/PR creation issues. Replace the existing Moodle image assets with official DGSHP/Ministry-approved artwork in a later asset-only workflow or local release-preparation step.

Recommended replacements:

- `resources/icon.png` — 1024×1024 source app icon.
- `resources/android/icon-foreground.png` — Android adaptive icon foreground source.
- `resources/splash.png` — splash source image.
- `resources/android/android-splash.xml` — Android 12+ splash vector.
- `src/assets/img/login_logo.png` — login logo shown before authentication.
- `src/assets/img/top_logo.png` — top logo used after authentication when configured.
- `src/assets/icon/icon.png` and `src/assets/icon/favicon.png` — web/runtime icons.
- `resources/android/icon/drawable-*-smallicon.png` — Android notification small icons; keep them simple and monochrome.

Avoid photographic imagery for app icons and splash screens. Keep artwork legible at small sizes and verify Android adaptive icon safe areas. Because the current PR avoids binary image diffs, these replacements should be handled outside this text-only PR path if the review system rejects binary files.

## Android local build

Required tools:

- Node.js `>=22.17 <23` (`.nvmrc` requests `lts/jod`)
- npm using `package-lock.json`
- JDK compatible with the Android Gradle plugin used by Cordova Android
- Android SDK command-line tools
- Android SDK platform for target SDK 36
- Android build tools

Typical setup/build commands:

```bash
nvm use
npm ci
npm run build:prod
npm run prod:android
```

For a local development run:

```bash
nvm use
npm ci
npm run dev:android
```

## Android test APK

The generated identity smoke-test APK is not checked in because binary artifacts can block pull request creation/review. If needed, generate it locally with `python scripts/create-identity-test-apk.py`; it verifies Android package/display-name metadata only and must not be uploaded to Google Play. See `release-artifacts/README.md` for details.

If Cordova/Android tooling is installed, generate the real Moodle App debug APK with a Cordova Android debug build, for example:

```bash
npx ionic cordova build android --debug
```

The exact APK path depends on Cordova/Gradle output, commonly under `platforms/android/app/build/outputs/apk/debug/`.

## Signed Android App Bundle for Google Play

1. Create or obtain the release keystore.
2. Store keystore passwords securely outside the repository.
3. Configure Cordova/Gradle signing with a local build config or environment-specific signing properties.
4. Build a release bundle, for example:

```bash
npx ionic cordova build android --prod --release -- --packageType=bundle
```

5. Verify the `.aab` under `platforms/android/app/build/outputs/bundle/release/`.
6. Upload the `.aab` to Google Play Console.

## Google Play signing preparation

- Decide whether Google Play App Signing will manage the app signing key.
- Create a unique upload key for this app.
- Do not commit keystores or signing passwords.
- Confirm the Android application ID is `org.santegovml.elearning` before the first production upload; changing it later creates a different app listing.
- Replace `google-services.json` with the final Firebase file if push notifications or Firebase services are required.

## iOS local build

Required tools:

- macOS
- Xcode
- CocoaPods
- Node.js `>=22.17 <23`
- npm dependencies installed with `npm ci`
- Apple Developer account access

Typical commands:

```bash
nvm use
npm ci
npm run build:prod
npm run prod:ios
```

You can also generate/open the Cordova iOS project and archive with Xcode.

## Xcode signing preparation

- Register bundle ID `org.santegovml.elearning` in the Apple Developer portal.
- Configure signing team, provisioning profiles, and capabilities.
- Configure push notification capability if notifications are required.
- Replace `GoogleService-Info.plist` with the final Firebase iOS file if push notifications or Firebase services are required.
- Confirm display name, icons, launch screen, privacy strings, and version/build numbers before archive.

## TestFlight and App Store Connect

1. Archive the iOS app in Xcode.
2. Validate the archive.
3. Upload to App Store Connect.
4. Complete TestFlight compliance and export/encryption questions.
5. Add internal testers first.
6. Run the release QA checklist.
7. Add App Store metadata, screenshots, privacy details, and review notes.
8. Submit for external TestFlight or App Store review.

## Keeping this fork updated from upstream Moodle App

Add upstream once in a full local clone:

```bash
git remote add upstream https://github.com/moodlehq/moodleapp.git
git fetch upstream
```

For future updates:

```bash
git checkout main
git fetch upstream
git merge upstream/main
```

Then reapply or resolve conflicts in the DGSHP-specific files listed above. Keep changes isolated to configuration, branding assets, and documentation where possible to preserve upstream compatibility.

