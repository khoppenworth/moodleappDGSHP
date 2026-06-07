# DGSHP e-Learning Store Readiness

## App identity

- App name: **DGSHP e-Learning**
- Android package ID: `org.santegovml.elearning`
- iOS bundle ID: `org.santegovml.elearning`
- Organization: Direction Générale de la Santé et de l'Hygiène Publique, Mali
- Primary language: French
- Secondary language: English
- Moodle site: `https://e-learning.santegovml.org/`

## French metadata

### Short description

Plateforme mobile de formation en ligne de la Direction Générale de la Santé et de l'Hygiène Publique du Mali.

### Full description

Application officielle de formation en ligne permettant aux professionnels de santé d’accéder aux cours, ressources, activités, évaluations et notifications de la plateforme e-learning de la Direction Générale de la Santé et de l'Hygiène Publique du Mali.

## English metadata

### Short description

Mobile e-learning platform for the Directorate General of Health and Public Hygiene of Mali.

### Full description

The official mobile learning application for health professionals using the e-learning platform of the Direction Générale de la Santé et de l'Hygiène Publique in Mali. The app provides access to courses, learning resources, activities, assessments, notifications, and supported offline learning features.

## Placeholder URLs

- Privacy policy URL: **TODO — provide official DGSHP or Ministry-approved privacy policy URL**
- Support URL: **TODO — provide official support/helpdesk URL or email landing page**
- Marketing URL: **TODO — provide official information page if available**

## Google Play assets

- Feature graphic: **TODO — create official 1024×500 Google Play feature graphic**
- Android screenshots: **TODO — capture final branded app screenshots on supported Android devices**
- App icon: existing Moodle image asset is not changed in this PR because binary image diffs can block PR creation; replace with final approved artwork before production
- Content rating notes: **TODO — complete Google Play content rating questionnaire**
- Data safety notes: **TODO — document account data, Moodle content access, notifications, offline storage, files, camera/media permissions, and analytics status**

## Apple App Store assets

- iPhone screenshots: **TODO — capture final branded iPhone screenshots**
- iPad screenshots: **TODO — capture final branded iPad screenshots if iPad distribution remains enabled**
- App icon: existing Moodle image asset is not changed in this PR because binary image diffs can block PR creation; replace with final approved artwork before production
- Content rating notes: **TODO — complete App Store age rating questionnaire**
- App privacy notes: **TODO — complete privacy nutrition labels based on final Moodle/Firebase/push configuration**

## Release notes placeholder

### French

Première version de l'application mobile DGSHP e-Learning pour accéder à la plateforme de formation en ligne de la Direction Générale de la Santé et de l'Hygiène Publique du Mali.

### English

Initial release of the DGSHP e-Learning mobile app for accessing the online learning platform of the Direction Générale de la Santé et de l'Hygiène Publique in Mali.

## Firebase and notifications

The repository contains placeholder Firebase configuration files updated to the new Android package and iOS bundle IDs. Replace these files with official Firebase project files before relying on push notifications:

- Android: `google-services.json`
- iOS: `GoogleService-Info.plist`

Notification support also depends on Moodle-side mobile notification configuration.

