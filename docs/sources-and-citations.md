# Sources & citations

Every mechanism shown in the diagrams is grounded in official platform documentation,
retrieved 24 September 2026.

## Google Ads / Google Marketing Platform

- **GCLID definition** — Google Click Identifier, a URL parameter passed with ad clicks; activated by auto-tagging; required for website conversion tracking.
  https://support.google.com/google-ads/answer/9744275
- **Auto-tagging** — appends the GCLID parameter to the URL customers click.
  https://support.google.com/google-ads/answer/1752125
  https://support.google.com/google-ads/answer/3095550
- **How Google Ads tracks website conversions** — the sitewide tag sets first-party cookies that store the user or the ad click (GCLID) that brought them to the site.
  https://support.google.com/google-ads/answer/7521212
- **Conversion Linker tag** (Google Tag Manager) — detects ad-click info in landing-page URLs and stores it in first-party cookies named `_gcl_*` such as `_gcl_aw` and `_gcl_gs`.
  https://support.google.com/tagmanager/answer/7549390
- **Google Ads conversions in GTM** — Conversion ID / Conversion Label / value.
  https://support.google.com/tagmanager/answer/6105160
- **Set up your Google tag in Google Ads**
  https://support.google.com/tagmanager/answer/15756614
- **Smart Bidding** — bidding strategies that use Google AI to optimise for conversions or conversion value in every auction.
  https://support.google.com/google-ads/answer/7065882
  https://support.google.com/google-ads/answer/11095984
- **Troubleshooting sitewide tagging** — the GCLID/AUID must be stored in a first-party cookie on the landing page and available on the conversion page.
  https://support.google.com/google-ads/answer/9148089

## Meta (Facebook / Instagram)

- **Advertising levels** — campaign, ad set, ad; what each controls.
  https://www.facebook.com/business/help/621956575422138
  https://www.facebook.com/business/help/613846972027099
- **ClickID and the `fbp` / `fbc` parameters** (Conversions API) — `fbclid` in the URL becomes the `fbc` parameter; the `_fbp` cookie supplies the browser ID (`fbp`).
  https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/fbp-and-fbc
- **Customer information parameters** — advanced matching fields sent with events.
  https://developers.facebook.com/documentation/ads-commerce/conversions-api/parameters/customer-information-parameters

## TikTok

- **Standard events and parameters** — events (PageView, AddToCart, CompletePayment…) used for reporting and optimisation.
  https://ads.tiktok.com/help/article/standard-events-parameters
- **TikTok API for Business** — `ttclid`, cookies and advanced matching used to attribute conversions and improve targeting/optimisation models.
  https://ads.tiktok.com/gateway/docs/index?identify_key=2b9b4278e47b275f36e7c39a4af4ba067d088e031d5f5fe45d381559ac89ba48&language=ENGLISH&doc_id=1727541103358977

## Notes on terminology in the diagrams

- **Click ID** — `gclid` (Google), `fbclid` (Meta), `ttclid` (TikTok). Appended to the
  landing-page URL on the ad click so the click can be matched to later conversions.
- **First-party click cookie** — `_gcl_aw` (Google), `_fbp` (Meta), `_ttp` (TikTok). The
  base/sitewide tag reads the URL click ID and stores it on the site's own domain so it
  survives navigation and can be attached to the conversion event.
- **Deduplication** — a shared `event_id` lets the browser pixel and the server-side API
  (CAPI / Events API) both fire without double-counting the same conversion.
- **Attribution window** — the period within which a click may receive credit for a
  conversion (platform defaults vary; e.g. Google 30-day click, Meta 7-day click / 1-day view).
- **Consent state** — observed live as `gcs=G111` (ad consent granted) vs `gcs=G100`
  (denied). Withholding ad storage consent suppresses the click-ID cookie and ad
  personalisation, which is why consent gating appears in the tag-architecture diagrams.
