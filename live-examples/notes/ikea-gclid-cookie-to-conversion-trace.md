# Step 2 — Retail: gclid captured, stored in cookie, traced to conversion (IKEA, 2026-09-24)

## Method
Landed on IKEA with a SYNTHETIC click ID to prove the mechanism without clicking
a paid ad (avoids billing an advertiser / click-fraud):
  https://www.ikea.com/gb/en/?gclid=DEMO_GCLID_20260924&utm_source=google&utm_medium=cpc

## 1. Consent gating (OneTrust / Optanon)
Before "Accept all": only 6 first-party cookies (IKEA's own + OptanonConsent).
NO `_gcl_*` and NO google-analytics network calls — the Google tag is consent-gated.

## 2. After "Accept all" — Google conversion linker reads the URL + writes cookie
First-party cookies created (document.cookie):
  `_gcl_aw` = GCL.1790293700.DEMO_GCLID_20260924   <-- THE CLICK ID, format GCL.<ts>.<gclid>
  `_gcl_au` = 1.1.1378351796.1790293700            <-- Google Ads user/linker ID (auid)
  `_ga`     = GA1.1.912322781.1790293700           <-- GA4 client id (cid)
  `_ga_S4EX53B760` = GS2.1.s1790293700...          <-- GA4 session
Also `_fbp` (Meta), `_pin_unauth` (Pinterest), `_uetsid`/`_uetvid` (Bing UET),
FPGSID (Yahoo), Optimizely, ContentSquare (_cs_*).

## 3. Tag payload echoes the click ID (page_view)
- googleadservices.com/pagead/set_partitioned_cookie?...&gclid=DEMO_GCLID_20260924
  &gclaw=DEMO_GCLID_20260924&gcs=G111&gcd=13t3t3t3t6l1&en=page_view&tid=DC-15866348
- ad.doubleclick.net/ccm/s/collect?gclid=DEMO_GCLID_20260924&auid=1378351796.1790293700
- sgtm.ikea.com/g/collect?v=2&tid=G-S4EX53B760&gcs=G111&cid=912322781.1790293700
  &en=page_view&dl=...gclid=DEMO_GCLID_20260924...&ep.query_parameter=gclid%3Ddemo...
  (GA4 via server-side GTM; IKEA even sends the raw query string as a custom param)

Decoded: `gclid` = click id · `gclaw` = gclid read from the _gcl_aw cookie ·
`gcs=G111` = Google conversion state (consent granted + click id present) ·
`auid` = _gcl_au cookie · `cid` = _ga client id.

## 4. Cookies persist across pages
On the product page the SAME cookies are still present:
  `_gcl_aw` = GCL.1790293700.DEMO_GCLID_20260924  (unchanged)

## 5. Product view (view_item) + Add to shopping bag
GA4 event `view_item` on DINERA mug (SKU 30362820, GBP 2.50):
  sgtm.ikea.com/g/collect?...&en=view_item&pr1=id30362820~k0product_buyable_online~v01...
Floodlight product view:
  ad.doubleclick.net/activity;src=15866348;type=produ0;cat=gb_cm002;...&u13=30362820&u16=2.5
Pinterest PageVisit with product + event_id.

## 6. Add-to-cart fires the conversion event + shared event_id
Pinterest AddToCart:
  ct.pinterest.com/v3/?event=AddToCart&ed={"event_id":"3f4fff36-5dba-42cf-bcf8-43f52ef13e47",
  "currency":"GBP","value":2.5,"line_items":[{"product_id":"30362820","quantity":1,
  "product_name":"DINERA","product_price":2.5}]}&tid=2618526101052&pd={"pin_unauth":...}
Doubleclick/Floodlight add-to-cart (same event_id -> DEDUP KEY):
  ad.doubleclick.net/activity;src=15866348;type=produ0;cat=gb_cm003;...
  &u25=3f4fff36-5dba-42cf-bcf8-43f52ef13e47&auiddc=1378351796.1790293700

## 7. TRACE-BACK PROOF: conversion pixel carries the click ID
Google Ads view-through conversion:
  googleads.g.doubleclick.net/pagead/viewthroughconversion/17648644137/
  ?en=conversion&label=vzqCCJr9-rkbEKngw99B
  &gclaw=DEMO_GCLID_20260924          <-- CLICK ID, read from _gcl_aw cookie
  &gclaw_src=6_7                      <-- source = first-party cookie
  &auid=1378351796.1790293700         <-- _gcl_au cookie
  &gcs=G111&gcd=13t3t3t3t7l1&gcl_ctr=1~0~0~0&data=event%3Dconversion
  &ct_cookie_present=false

CHAIN VERIFIED END-TO-END:
  URL ?gclid=DEMO_GCLID_20260924
    -> _gcl_aw cookie GCL.1790293700.DEMO_GCLID_20260924   (base tag / conversion linker)
    -> event_id 3f4fff36-5dba-42cf-bcf8-43f52ef13e47        (add_to_cart, shared/deduped)
    -> Google Ads conversion pixel &gclaw=DEMO_GCLID_20260924&en=conversion
  This is the D2/D4/D6 diagrams proven live: click id -> cookie -> event -> attributed conversion.

## Notes
- `_gcl_aw` value format `GCL.<expiry-timestamp>.<gclid>` is Google's documented
  first-party storage for the Google Click Identifier (see Conversion Linker docs).
- `gcs=G111` = G1 (consent) 11 (all purposes) + 1 (click id available). When consent
  is denied this degrades (e.g. G101 / G1--) and the click id may not be sent.
- `event_id` (3f4fff36...) is the cross-tag dedup key: the browser pixel + server/site
  events reuse it so the same add_to_cart isn't double-counted (the D2/D5 diagram).
