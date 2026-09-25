# Step 3 — REAL Google Ads gclid, traced live (Google Search -> MoneySuperMarket, 2026-09-24)

A genuine paid Google Ads search click (one click only). This is the real-gclid
counterpart to the synthetic IKEA demo in `02_...`.

## 1. The ad
Google Search `car insurance quotes` (UK). 4 "Sponsored Results" text ads at top.
Selected advertiser: **MoneySuperMarket** ("Compare Cheap Car Insurance UK | Up To £483").
Ad link = Google ad-click server, not the destination directly.

## 2. The click URL carries the gclid BEFORE the click (in the DOM)
  https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChsSEwinluGTv4iXAxV8xnkEHUQkM4UYA...
    &gclid=EAIaIQobChMIp5bhk7-IlwMVfMZ5BB1EJDOFEAAYASABEgIKuPD_BwE
    &cid=CAASsAHkaDarkl3IoM0s...
  (also google.com/aclk variants; `gclid` is a real Google Click ID.)

REAL GCLID:  EAIaIQobChMIp5bhk7-IlwMVfMZ5BB1EJDOFEAAYASABEgIKuPD_BwE

## 3. Click fires the click-through beacon
  GET  googleadservices.com/pagead/aclk?...&gclid=<above>&category=acrcp_v1_71...  -> 204
  POST google.com/aclk?...&gclid=<above>&act=1&ri=1&suid=86229756409... (click logged)

## 4. Landing URL carries the SAME gclid + Google Ads metadata
  https://www.moneysupermarket.com/car-insurance/
    ?utm_source=google&utm_medium=cpc&utm_campaign=23738350763
     &utm_id=23738350763&utm_term=car%20insurance%20quotes
     &gclsrc=aw.ds
     &source=GOO-0X0000048C2DEA5BA7
     &gad_source=1&gad_campaignid=23738350763
     &gbraid=0AAAAAD4DchDJeq7oTd8mWgWfXLA94JDei
     &gclid=EAIaIQobChMIp5bhk7-IlwMVfMZ5BB1EJDOFEAAYASABEgIKuPD_BwE   <-- SAME gclid

Decoded landing params:
  gclid          = the click id (identical to the one in the ad aclk URL)  <-- PROOF
  gclsrc=aw.ds   = Google Ads source marker (AdWords/auto-tagging)
  gad_source=1   = Google Ads traffic source (1 = Paid Search)
  gad_campaignid = 23738350763 (the Google Ads campaign)
  gbraid         = 0AAAAAD4DchDJeq7oTd8mWgWfXLA94JDei (privacy-era web/app click id,
                   the "braid" companion to gclid)
  utm_*          = auto-tagging ALSO appended campaign UTMs (utm_source=google,
                   utm_medium=cpc, utm_campaign=23738350763, utm_term=car insurance quotes)
  source=GOO-... = MoneySuperMarket's own first-party tracking code

## 5. GA4 (server-side GTM) captures the full landing URL incl. the gclid
  tags.moneysupermarket.com/g/collect?v=2&tid=G-G6KGF29JVK
    &gcs=G100&gcd=13p3p3p3p5l1&npa=1&pscdl=denied&ecid=262419283
    &cid=156435812.1790296957&en=page_view
    &dl=https://www.moneysupermarket.com/car-insurance/?...&gclid=EAIaIQobChMIp5bhk7-IlwMVfMZ5BB1EJDOFEAAYASABEgIKuPD_BwE
    &dr=https://www.google.com/   (referrer = google)

## 6. Consent state observed (great teaching point)
  MoneySuperMarket page_view:  gcs=G100, npa=1, psccdl=denied
    -> G1 00 = ads storage/consent DENIED -> conversion linker did NOT write _gcl_aw;
       ad personalisation off (npa=1). The gclid is still in the URL + GA4 `dl=`, but
       click-based ad conversion is restricted.
  Compare IKEA (where I accepted all):  gcs=G111, npa=0 -> _gcl_aw WAS written.
  This is exactly the D4/D6 "consent gates the signal" behaviour.

## VERDICT
The core mechanic is proven with a REAL gclid:
  Google Ads ad (gclid generated + logged at click)
    -> redirect to landing page with the SAME gclid in the URL
    -> GA4/tag reads the URL and forwards it to measurement
    -> (with ad consent) Google conversion linker stores it in _gcl_aw and the
       conversion pixel later returns gclaw=<gclid> (as shown synthetically in step 2).
This matches the v2/D2 "click ID appended to URL" and v4/D4 "base tag stores it" diagrams.
