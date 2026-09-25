# Step 1 — Publisher ad click chain (The Guardian, 2026-09-24)

## Cookie state BEFORE consent
6 first-party cookies: gu_client_ab_tests, gu_v2_mvt_id, GU_mvt_id, GU_geo_country,
bwid (SourcePoint browser id), consentUUID (SourcePoint consent id).

## Cookie state AFTER "Accept all" (SourcePoint, 139 partners)
24 first-party cookies. New ad-tech IDs appeared:
- `_pubcid` = 9b995ace-43fe-45c8-a84a-9f8961c9db1a  (SharedID / PubCommon, IAB)
- `permutive-id` = 69c4b943-978f-445e-a9d5-eec596215583 (Permutive DMP)
- `panoramaId` (LiveRamp ATS identity)
- `connectId` (Yahoo identity)
- `__gads` = ID=a350d919bdf6e220:T=...:S=ALNI_... (Google Ads cookie)
- `__gpi` = UID=0000152216702b7f:T=... (Google Publisher ID)
- `__eoi` = ID=2a20d468ca6cecba:T=... (Google Enhanced/EEA identity)
- `cto_bundle`, `_cc_id` (Criteo)
- `_scor_uid` (ScorecardResearch)
- `DotMetrics.DomainCookie`, `panoramaId_expiry`, `_pubcid_cst`, `_lr_sampling_rate`

## Network: full programmatic auction on page load
Prebid.js bid requests to Rubicon (fastlane.rubiconproject.com), PubMatic
(hbopenbid.pubmatic.com), The Ozone Project (elb.the-ozone-project.com), Criteo
(grid-bidder.criteo.com), OpenX (rtb.openx.net), Teads (a.teads.tv), AppNexus
(ib.adnxs.com), Index/TTD via GAM. Amazon APS header bidding
(c.amazon-adsystem.com + web-banner.ads.aps.amazon-adsystem.com/dtb/bid).
Permutive cohort + geoip + affinity calls. Google Ad Manager ad serving
(securepubads.g.doubleclick.net/gampad/ads). Viewability pings
(pagead2.googlesyndication.com/pcs/activeview, doubleclick /pcs/view).

## COOKIE -> AD REQUEST TRACE (this is the money shot)
The GAM ad request echoes first-party cookie values as URL params:
- `__gads` cookie value  -> `cookie=ID=a350d919bdf6e220:T=...:S=ALNI_...`
- `__gpi` cookie value  -> `gpic=UID=0000152216702b7f:T=...`
- `__eoi` cookie value  -> `eo_id_str=ID=2a20d468ca6cecba:T=...`
- `permutive-id` cookie -> `cust_params=...puid=69c4b943-978f-445e-a9d5-eec596215583...`
Also passes `pubcid.org=9b995ace-...` (the `_pubcid`) to Ozone + Rubicon.

## Ad slot + click URL
Slot: `dfp-ad--top-above-nav`, ad unit `/59666047/theguardian.com/international/front/ng`,
GPID `/59666047/gu/international/Network Front/top-above-nav`.
Creative lives in iframe `google_ads_iframe_/59666047/theguardian.com/international/front/ng_0`.
Click anchor href:
  https://googleads.g.doubleclick.net/pcs/click?xai=AKAOjstcK3b...&sai=AMfl-YSW...
  &sig=Cg0ArKJSzHDNGp1fA_BA&fbs_aeid=[gw_fbsaeid]
  &adurl=https://www.theguardian.com/education/ng-interactive/2025/sep/13/
         the-guardian-university-guide-2026-the-rankings
         %3Futm_source%3Dodpy%26utm_medium%3Ddispad%26utm_campaign%3Duniguide_billboard

`adurl` decodes to the destination with UTM params:
  utm_source=odpy  utm_medium=dispad  utm_campaign=uniguide_billboard
So the click server (doubleclick /pcs/click) records the click, then 302s to the
advertiser's landing page carrying attribution params (UTM here; a Google Ads
conversion-tracked campaign would carry `gclid`).
