# DGSHP e-Learning Release QA Checklist

Use this checklist before each release candidate and store submission.

## Launch and branding

- [ ] App launches correctly.
- [ ] App name is **DGSHP e-Learning** on Android.
- [ ] App name is **DGSHP e-Learning** on iOS.
- [ ] App icon appears correctly on Android.
- [ ] App icon appears correctly on iOS.
- [ ] Splash screen appears correctly on Android.
- [ ] Splash screen appears correctly on iOS.
- [ ] Login screen branding appears correctly.
- [ ] Top logo appears correctly after login when the Moodle site provides/permits it.

## Moodle site login

- [ ] Login points to `https://e-learning.santegovml.org/`.
- [ ] User does not need to type the site URL manually.
- [ ] Invalid/other site URLs are blocked or documented according to the fixed-site configuration.
- [ ] Username/password login works.
- [ ] SSO login works, if enabled on the Moodle site.
- [ ] Logout and reconnect flows work.

## Languages

- [ ] French interface works.
- [ ] English interface works.
- [ ] French remains the default language for first launch.
- [ ] Language switching works if enabled.

## Moodle learning features

- [ ] Course categories display correctly.
- [ ] Courses open correctly.
- [ ] Course sections and activities display correctly.
- [ ] Learning resources open correctly.
- [ ] H5P activities load correctly.
- [ ] Quizzes work.
- [ ] Assignments work.
- [ ] Grades display correctly.
- [ ] Messaging works.
- [ ] Calendar/reminders work where configured.
- [ ] File upload/download behavior works where permissions are granted.

## Notifications

- [ ] Notifications are tested on Android, or documented as pending Moodle/Firebase configuration.
- [ ] Notifications are tested on iOS, or documented as pending Moodle/Firebase/APNs configuration.
- [ ] Notification small icon appears correctly on Android.
- [ ] Notification permission prompts are appropriate.

## Offline behavior

- [ ] Offline-supported course content downloads correctly.
- [ ] Downloaded content opens while offline.
- [ ] Offline actions synchronize after reconnecting.
- [ ] Storage management screen behaves correctly.

## Android builds

- [ ] Android debug/test APK build completed, if supported by local tooling.
- [ ] Android APK smoke test completed on a physical device or emulator.
- [ ] Android signed AAB release build completed, if signing credentials are available.
- [ ] Google Play upload key and signing configuration are documented and stored securely.
- [ ] Final `google-services.json` is in place if notifications/Firebase are required.

## iOS builds

- [ ] iOS build completed on macOS/Xcode, or remaining Apple signing/account requirements are clearly documented.
- [ ] iOS archive completed in Xcode.
- [ ] TestFlight upload completed.
- [ ] Final `GoogleService-Info.plist` is in place if notifications/Firebase are required.
- [ ] Apple bundle ID, signing team, provisioning profile, and capabilities are confirmed.

## Store readiness

- [ ] Privacy policy URL finalized.
- [ ] Support URL finalized.
- [ ] Marketing URL finalized, if needed.
- [ ] Google Play feature graphic prepared.
- [ ] Android screenshots prepared.
- [ ] iPhone screenshots prepared.
- [ ] iPad screenshots prepared, if required.
- [ ] Content rating completed.
- [ ] Data safety / app privacy forms completed.
- [ ] Release notes finalized in French and English.

