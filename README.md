# Ad Pixel & Conversion Tracking Diagrams

A visual, sourced explainer of the end-to-end loop from **launching a campaign** → **user sees & clicks the ad** (cookies dropped, `gclid` / `fbclid` / `ttclid` appended) → **lands on site** (base tag reads the click ID into a first-party cookie) → **converts** (event tag fires with the stored click ID) → **conversion recorded** → **the algorithm learns** → **campaign optimisation improves**.

Written for people who understand ads but not the technical plumbing underneath.

## What is in this repo

| Folder | Contents |
|---|---|

| `sources/excalidraw/` | 14 editable **Excalidraw** scenes (`.excalidraw`) |

| `sources/drawio/` | One **draw.io** file with 7 pages (`.drawio`) covering the standard set |

| `images/svg/` | 21 **SVG** renders (14 from Excalidraw + 7 draw.io pages) |

| `images/png/` | 21 **PNG** renders of the same diagrams |

| `live-examples/screenshots/` | Real browser captures (Guardian, IKEA, MoneySuperMarket) |

| `live-examples/annotated/` | The same captures with callouts pointing at the tracking evidence |

| `live-examples/notes/` | Full cookie lists, decoded tag payloads and click chains |

| `docs/sources-and-citations.md` | Official documentation behind every claim |


### File-naming convention

Every filename states **what the diagram shows**, **which series it belongs to**, and (for renders) **which tool produced it**:

```
<series>-<nn>-<what-it-shows>--<tool>.<ext>
```

- **series**: `standard` = consistent left-to-right teaching layout; `varied` = a layout shaped by the concept (cycle, tree, timeline, gears, funnel, swimlanes, decision tree)

- **tool**: `excalidraw` or `drawio` — so you can tell which source a render came from

- live-example files lead with the **site name** (`guardian-`, `ikea-`, `moneysupermarket-`) and a step number


---

# Part 1 — Standard-layout diagram set

A left-to-right teaching sequence. Start at 01 and read down. Also available as a single 7-page draw.io file: [`standard-01-to-07-ad-tracking-diagram-set.drawio`](sources/drawio/standard-01-to-07-ad-tracking-diagram-set.drawio).


### Master View — End-to-End Ad Conversion & Optimisation Loop

The all-encompassing master diagram. Every actor, signal and handoff from campaign launch through algorithm optimisation, in four bands: campaign setup, tag deployment, live traffic, and conversion & feedback.


**Excalidraw render**

![Master View — End-to-End Ad Conversion & Optimisation Loop — Excalidraw SVG](images/svg/standard-01-master-ad-conversion-optimisation-loop-excalidraw.svg)

![Master View — End-to-End Ad Conversion & Optimisation Loop — Excalidraw PNG](images/png/standard-01-master-ad-conversion-optimisation-loop-excalidraw.png)


**draw.io render**

![Master View — End-to-End Ad Conversion & Optimisation Loop — draw.io SVG](images/svg/standard-01-master-ad-conversion-optimisation-loop-drawio.svg)

![Master View — End-to-End Ad Conversion & Optimisation Loop — draw.io PNG](images/png/standard-01-master-ad-conversion-optimisation-loop-drawio.png)

**Files:** [`standard-01-master-ad-conversion-optimisation-loop.excalidraw`](sources/excalidraw/standard-01-master-ad-conversion-optimisation-loop.excalidraw) · [SVG (excalidraw)](images/svg/standard-01-master-ad-conversion-optimisation-loop-excalidraw.svg) · [PNG (excalidraw)](images/png/standard-01-master-ad-conversion-optimisation-loop-excalidraw.png) · [SVG (drawio)](images/svg/standard-01-master-ad-conversion-optimisation-loop-drawio.svg) · [PNG (drawio)](images/png/standard-01-master-ad-conversion-optimisation-loop-drawio.png)


### Campaign Structure & Launch Setup

What an advertiser configures and what the platform needs to run the ad: campaign ▸ ad set / ad group ▸ ad, plus the tracking template (gclid / fbclid / ttclid + UTM) and the click-ID cookie layer.


**Excalidraw render**

![Campaign Structure & Launch Setup — Excalidraw SVG](images/svg/standard-02-campaign-structure-and-launch-setup-excalidraw.svg)

![Campaign Structure & Launch Setup — Excalidraw PNG](images/png/standard-02-campaign-structure-and-launch-setup-excalidraw.png)


**draw.io render**

![Campaign Structure & Launch Setup — draw.io SVG](images/svg/standard-02-campaign-structure-and-launch-setup-drawio.svg)

![Campaign Structure & Launch Setup — draw.io PNG](images/png/standard-02-campaign-structure-and-launch-setup-drawio.png)

**Files:** [`standard-02-campaign-structure-and-launch-setup.excalidraw`](sources/excalidraw/standard-02-campaign-structure-and-launch-setup.excalidraw) · [SVG (excalidraw)](images/svg/standard-02-campaign-structure-and-launch-setup-excalidraw.svg) · [PNG (excalidraw)](images/png/standard-02-campaign-structure-and-launch-setup-excalidraw.png) · [SVG (drawio)](images/svg/standard-02-campaign-structure-and-launch-setup-drawio.svg) · [PNG (drawio)](images/png/standard-02-campaign-structure-and-launch-setup-drawio.png)


### Conversion Signal Flow — Click to Recorded Conversion

How a browser-side action is linked back to a specific ad click: the click journey, the conversion journey, and the learning loop.


**Excalidraw render**

![Conversion Signal Flow — Click to Recorded Conversion — Excalidraw SVG](images/svg/standard-03-conversion-signal-flow-click-to-conversion-excalidraw.svg)

![Conversion Signal Flow — Click to Recorded Conversion — Excalidraw PNG](images/png/standard-03-conversion-signal-flow-click-to-conversion-excalidraw.png)


**draw.io render**

![Conversion Signal Flow — Click to Recorded Conversion — draw.io SVG](images/svg/standard-03-conversion-signal-flow-click-to-conversion-drawio.svg)

![Conversion Signal Flow — Click to Recorded Conversion — draw.io PNG](images/png/standard-03-conversion-signal-flow-click-to-conversion-drawio.png)

**Files:** [`standard-03-conversion-signal-flow-click-to-conversion.excalidraw`](sources/excalidraw/standard-03-conversion-signal-flow-click-to-conversion.excalidraw) · [SVG (excalidraw)](images/svg/standard-03-conversion-signal-flow-click-to-conversion-excalidraw.svg) · [PNG (excalidraw)](images/png/standard-03-conversion-signal-flow-click-to-conversion-excalidraw.png) · [SVG (drawio)](images/svg/standard-03-conversion-signal-flow-click-to-conversion-drawio.svg) · [PNG (drawio)](images/png/standard-03-conversion-signal-flow-click-to-conversion-drawio.png)


### Algorithm Learning Loop

How conversion data trains the model: signal accumulation → pattern learning → auction-level optimisation → measurable outcome.


**Excalidraw render**

![Algorithm Learning Loop — Excalidraw SVG](images/svg/standard-04-algorithm-learning-loop-excalidraw.svg)

![Algorithm Learning Loop — Excalidraw PNG](images/png/standard-04-algorithm-learning-loop-excalidraw.png)


**draw.io render**

![Algorithm Learning Loop — draw.io SVG](images/svg/standard-04-algorithm-learning-loop-drawio.svg)

![Algorithm Learning Loop — draw.io PNG](images/png/standard-04-algorithm-learning-loop-drawio.png)

**Files:** [`standard-04-algorithm-learning-loop.excalidraw`](sources/excalidraw/standard-04-algorithm-learning-loop.excalidraw) · [SVG (excalidraw)](images/svg/standard-04-algorithm-learning-loop-excalidraw.svg) · [PNG (excalidraw)](images/png/standard-04-algorithm-learning-loop-excalidraw.png) · [SVG (drawio)](images/svg/standard-04-algorithm-learning-loop-drawio.svg) · [PNG (drawio)](images/png/standard-04-algorithm-learning-loop-drawio.png)


### Cookies & Click IDs Deep Dive

gclid / fbclid / ttclid appended to the URL → first-party cookies (_gcl_aw / _fbp / _ttp) → matching the conversion event to the click.


**Excalidraw render**

![Cookies & Click IDs Deep Dive — Excalidraw SVG](images/svg/standard-05-cookies-and-click-ids-excalidraw.svg)

![Cookies & Click IDs Deep Dive — Excalidraw PNG](images/png/standard-05-cookies-and-click-ids-excalidraw.png)


**draw.io render**

![Cookies & Click IDs Deep Dive — draw.io SVG](images/svg/standard-05-cookies-and-click-ids-drawio.svg)

![Cookies & Click IDs Deep Dive — draw.io PNG](images/png/standard-05-cookies-and-click-ids-drawio.png)

**Files:** [`standard-05-cookies-and-click-ids.excalidraw`](sources/excalidraw/standard-05-cookies-and-click-ids.excalidraw) · [SVG (excalidraw)](images/svg/standard-05-cookies-and-click-ids-excalidraw.svg) · [PNG (excalidraw)](images/png/standard-05-cookies-and-click-ids-excalidraw.png) · [SVG (drawio)](images/svg/standard-05-cookies-and-click-ids-drawio.svg) · [PNG (drawio)](images/png/standard-05-cookies-and-click-ids-drawio.png)


### Tag Setup & GTM Deep Dive

Base tags on every page vs event tags on converting pages vs the server-side layer (CAPI / Events API), laid out per platform (Google, Meta, TikTok).


**Excalidraw render**

![Tag Setup & GTM Deep Dive — Excalidraw SVG](images/svg/standard-06-tag-setup-and-gtm-excalidraw.svg)

![Tag Setup & GTM Deep Dive — Excalidraw PNG](images/png/standard-06-tag-setup-and-gtm-excalidraw.png)


**draw.io render**

![Tag Setup & GTM Deep Dive — draw.io SVG](images/svg/standard-06-tag-setup-and-gtm-drawio.svg)

![Tag Setup & GTM Deep Dive — draw.io PNG](images/png/standard-06-tag-setup-and-gtm-drawio.png)

**Files:** [`standard-06-tag-setup-and-gtm.excalidraw`](sources/excalidraw/standard-06-tag-setup-and-gtm.excalidraw) · [SVG (excalidraw)](images/svg/standard-06-tag-setup-and-gtm-excalidraw.svg) · [PNG (excalidraw)](images/png/standard-06-tag-setup-and-gtm-excalidraw.png) · [SVG (drawio)](images/svg/standard-06-tag-setup-and-gtm-drawio.svg) · [PNG (drawio)](images/png/standard-06-tag-setup-and-gtm-drawio.png)


### Attribution Deep Dive

Match rules, deduplication (shared event_id), and what happens when signals are missing — modelled conversions and consent/privacy gaps.


**Excalidraw render**

![Attribution Deep Dive — Excalidraw SVG](images/svg/standard-07-attribution-deep-dive-excalidraw.svg)

![Attribution Deep Dive — Excalidraw PNG](images/png/standard-07-attribution-deep-dive-excalidraw.png)


**draw.io render**

![Attribution Deep Dive — draw.io SVG](images/svg/standard-07-attribution-deep-dive-drawio.svg)

![Attribution Deep Dive — draw.io PNG](images/png/standard-07-attribution-deep-dive-drawio.png)

**Files:** [`standard-07-attribution-deep-dive.excalidraw`](sources/excalidraw/standard-07-attribution-deep-dive.excalidraw) · [SVG (excalidraw)](images/svg/standard-07-attribution-deep-dive-excalidraw.svg) · [PNG (excalidraw)](images/png/standard-07-attribution-deep-dive-excalidraw.png) · [SVG (drawio)](images/svg/standard-07-attribution-deep-dive-drawio.svg) · [PNG (drawio)](images/png/standard-07-attribution-deep-dive-drawio.png)


---

# Part 2 — Varied-layout diagram set

The same subject matter, but each diagram uses a layout that matches its idea — so it is not seven identical box chains.


### The Ad Conversion Loop (circular cycle)

The full loop drawn as a circle: setup → tracking built → live traffic → conversion, with the algorithm at the hub learning from every pass.

**Excalidraw render**

![The Ad Conversion Loop (circular cycle) — SVG](images/svg/varied-01-ad-conversion-loop-cycle-excalidraw.svg)

![The Ad Conversion Loop (circular cycle) — PNG](images/png/varied-01-ad-conversion-loop-cycle-excalidraw.png)

**Files:** [`varied-01-ad-conversion-loop-cycle.excalidraw`](sources/excalidraw/varied-01-ad-conversion-loop-cycle.excalidraw) · [SVG](images/svg/varied-01-ad-conversion-loop-cycle-excalidraw.svg) · [PNG](images/png/varied-01-ad-conversion-loop-cycle-excalidraw.png)


### Campaign Anatomy (hierarchy tree)

Campaign → budget / objective / bidding strategy → ad sets → ads, shown as a branching tree with what each level controls.

**Excalidraw render**

![Campaign Anatomy (hierarchy tree) — SVG](images/svg/varied-02-campaign-anatomy-hierarchy-tree-excalidraw.svg)

![Campaign Anatomy (hierarchy tree) — PNG](images/png/varied-02-campaign-anatomy-hierarchy-tree-excalidraw.png)

**Files:** [`varied-02-campaign-anatomy-hierarchy-tree.excalidraw`](sources/excalidraw/varied-02-campaign-anatomy-hierarchy-tree.excalidraw) · [SVG](images/svg/varied-02-campaign-anatomy-hierarchy-tree-excalidraw.svg) · [PNG](images/png/varied-02-campaign-anatomy-hierarchy-tree-excalidraw.png)


### Six Seconds Inside the Click (vertical timeline)

A time-stamped vertical spine from T+0ms ad click through click-ID append, landing, cookie write, conversion, to the recorded credit.

**Excalidraw render**

![Six Seconds Inside the Click (vertical timeline) — SVG](images/svg/varied-03-click-journey-vertical-timeline-excalidraw.svg)

![Six Seconds Inside the Click (vertical timeline) — PNG](images/png/varied-03-click-journey-vertical-timeline-excalidraw.png)

**Files:** [`varied-03-click-journey-vertical-timeline.excalidraw`](sources/excalidraw/varied-03-click-journey-vertical-timeline.excalidraw) · [SVG](images/svg/varied-03-click-journey-vertical-timeline-excalidraw.svg) · [PNG](images/png/varied-03-click-journey-vertical-timeline-excalidraw.png)


### The Learning Cycle (overlapping gears)

Data in → patterns out → auction bids → outcome, drawn as four overlapping gears around the central model.

**Excalidraw render**

![The Learning Cycle (overlapping gears) — SVG](images/svg/varied-04-learning-cycle-gears-excalidraw.svg)

![The Learning Cycle (overlapping gears) — PNG](images/png/varied-04-learning-cycle-gears-excalidraw.png)

**Files:** [`varied-04-learning-cycle-gears.excalidraw`](sources/excalidraw/varied-04-learning-cycle-gears.excalidraw) · [SVG](images/svg/varied-04-learning-cycle-gears-excalidraw.svg) · [PNG](images/png/varied-04-learning-cycle-gears-excalidraw.png)


### Where the Click ID Lives (storage layers)

Three storage layers — URL, first-party cookie, platform backend — each holding part of the attribution puzzle, and why all three are needed.

**Excalidraw render**

![Where the Click ID Lives (storage layers) — SVG](images/svg/varied-05-click-id-storage-layers-excalidraw.svg)

![Where the Click ID Lives (storage layers) — PNG](images/png/varied-05-click-id-storage-layers-excalidraw.png)

**Files:** [`varied-05-click-id-storage-layers.excalidraw`](sources/excalidraw/varied-05-click-id-storage-layers.excalidraw) · [SVG](images/svg/varied-05-click-id-storage-layers-excalidraw.svg) · [PNG](images/png/varied-05-click-id-storage-layers-excalidraw.png)


### Tag Architecture (stacked swimlanes)

Browser → internet → platform server, showing what runs where: base tag, cookie layer, event tag, dedup layer, server-side API, matching engine.

**Excalidraw render**

![Tag Architecture (stacked swimlanes) — SVG](images/svg/varied-06-tag-architecture-swimlanes-excalidraw.svg)

![Tag Architecture (stacked swimlanes) — PNG](images/png/varied-06-tag-architecture-swimlanes-excalidraw.png)

**Files:** [`varied-06-tag-architecture-swimlanes.excalidraw`](sources/excalidraw/varied-06-tag-architecture-swimlanes.excalidraw) · [SVG](images/svg/varied-06-tag-architecture-swimlanes-excalidraw.svg) · [PNG](images/png/varied-06-tag-architecture-swimlanes-excalidraw.png)


### How a Conversion Gets Credited (decision tree)

Decision gates from click-ID match through attribution window and event_id dedup to the credited conversion.

**Excalidraw render**

![How a Conversion Gets Credited (decision tree) — SVG](images/svg/varied-07-attribution-decision-tree-excalidraw.svg)

![How a Conversion Gets Credited (decision tree) — PNG](images/png/varied-07-attribution-decision-tree-excalidraw.png)

**Files:** [`varied-07-attribution-decision-tree.excalidraw`](sources/excalidraw/varied-07-attribution-decision-tree.excalidraw) · [SVG](images/svg/varied-07-attribution-decision-tree-excalidraw.svg) · [PNG](images/png/varied-07-attribution-decision-tree-excalidraw.png)


---

# Part 3 — Live "in the wild" evidence

Real browser-automation captures that back up the diagrams. Full cookie lists and decoded payloads are in [`live-examples/notes/`](live-examples/notes/).


### Guardian — page load + consent banner

SourcePoint consent dialog (139 partners) before any ad-tech fires.

![Guardian — page load + consent banner](live-examples/screenshots/guardian-01-page-load-and-cookie-banner.png)


### Guardian — live display ad + post-consent cookies (annotated)

A live Google Ad Manager display ad in the top-above-nav slot; 24 ad-tech cookies after "Accept all"; full Prebid auction to 8+ SSPs.

![Guardian — live display ad + post-consent cookies (annotated)](live-examples/annotated/guardian-02-ad-served-cookies-after-consent-ANNOTATED.png)


### Guardian — live display ad + post-consent cookies (raw)

Un-annotated capture of the same state.

![Guardian — live display ad + post-consent cookies (raw)](live-examples/screenshots/guardian-02-ad-served-cookies-after-consent.png)


### Guardian — landing page after ad click (annotated)

URL carries UTM params; the __gads cookie timestamp advanced (base tag read + refreshed it); the ad request still echoes cookie IDs.

![Guardian — landing page after ad click (annotated)](live-examples/annotated/guardian-03-landing-page-after-ad-click-ANNOTATED.png)


### Guardian — landing page after ad click (raw)

Un-annotated capture of the same state.

![Guardian — landing page after ad click (raw)](live-examples/screenshots/guardian-03-landing-page-after-ad-click.png)


### IKEA — consent-gated tags

OneTrust / OptanonConsent banner. Before "Accept all" the Google tag does not fire and no _gcl_* cookies exist.

![IKEA — consent-gated tags](live-examples/screenshots/ikea-04-cookie-banner-consent-gated-tags.png)


### IKEA — product page before add-to-cart (annotated)

_gcl_aw = GCL.1790293700.DEMO_GCLID_20260924 persists across pages (click-ID cookie survives navigation); view_item fires.

![IKEA — product page before add-to-cart (annotated)](live-examples/annotated/ikea-05-product-page-before-add-to-cart-ANNOTATED.png)


### IKEA — product page before add-to-cart (raw)

Un-annotated capture of the same state.

![IKEA — product page before add-to-cart (raw)](live-examples/screenshots/ikea-05-product-page-before-add-to-cart.png)


### IKEA — add-to-cart conversion fired (annotated)

The add_to_cart drawer. Google Ads viewthroughconversion pixel carries gclaw=DEMO_GCLID_20260924; Pinterest AddToCart + DoubleClick Floodlight share one event_id for dedup.

![IKEA — add-to-cart conversion fired (annotated)](live-examples/annotated/ikea-06-add-to-cart-conversion-fired-ANNOTATED.png)


### IKEA — add-to-cart conversion fired (raw)

Un-annotated capture of the same state.

![IKEA — add-to-cart conversion fired (raw)](live-examples/screenshots/ikea-06-add-to-cart-conversion-fired.png)


### MoneySuperMarket — REAL gclid landing page (annotated)

A live Google Ads search click. The same real gclid appears in the ad aclk URL and on the landing URL; GA4 server-side g/collect forwards it.

![MoneySuperMarket — REAL gclid landing page (annotated)](live-examples/annotated/moneysupermarket-08-real-gclid-landing-page-ANNOTATED.png)


### MoneySuperMarket — REAL gclid landing page (raw)

Un-annotated capture of the same state.

![MoneySuperMarket — REAL gclid landing page (raw)](live-examples/screenshots/moneysupermarket-08-real-gclid-landing-page.png)


### Live-example write-ups

- [`guardian-publisher-ad-click-chain.md`](live-examples/notes/guardian-publisher-ad-click-chain.md) — publisher ad click chain + cookie→ad-request trace

- [`ikea-gclid-cookie-to-conversion-trace.md`](live-examples/notes/ikea-gclid-cookie-to-conversion-trace.md) — synthetic gclid → `_gcl_aw` cookie → conversion pixel

- [`real-gclid-live-google-ads-click-trace.md`](live-examples/notes/real-gclid-live-google-ads-click-trace.md) — a real Google Ads gclid traced from click to landing URL


---

# Part 4 — Editorial set (`diagram-design` skill)

A second, independent set built with the [diagram-design](https://github.com/cathrynlavery/diagram-design)
skill (self-contained HTML + inline SVG, editorial design system). The existing
Excalidraw and draw.io sets above are preserved unchanged; this set is additive.

**Why a second set:** the first set used one layout habit (left-to-right box chains).
This set picks a *diagram grammar per idea*, so each visual is shaped by what it
has to explain rather than by a single default.

## Type selection — one grammar per dominant axis

| # | Diagram | Grammar chosen | Why this grammar |
|---|---------|----------------|------------------|
| `01-master-cross-functional-handoff` | Master view: who does what, end to end | Swimlane |
| `02-campaign-anatomy` | Campaign anatomy: each level has one job | Tree |
| `03-click-to-conversion-messages` | The click as messages between five actors | Sequence |
| `04-click-journey-timeline` | Six seconds inside the click | Timeline |
| `05-algorithm-learning-loop` | How the algorithm learns from every conversion | Loop |
| `06-where-click-id-lives` | Where the click ID actually lives | Layer stack |
| `07-tag-architecture` | Tag architecture: what runs where | Architecture |
| `08-attribution-decision-flow` | How a conversion gets credited | Flowchart |

Planned cuts (per the skill's deletion rule): one focused visual per idea instead of
reproducing all 14 earlier diagrams. Every diagram stays within the skill's complexity
budget (≤9 nodes, ≤12 connectors, ≤2 coral accents) and `doc-wide` 1280×720 so the set
drops straight into a deck.

## The diagrams

### Master view: who does what, end to end

**Swimlane** — cross-functional handoffs are the story, so the layout is horizontal lanes (Advertiser → Ad platform → Browser → Website → Measurement). Coral marks the two moments attribution depends on: the click ID and the credited conversion.

![Master view: who does what, end to end](images/svg/editorial-01-master-cross-functional-handoff--diagramdesign.svg)

**Files:** [`01-master-cross-functional-handoff--diagramdesign.html`](sources/diagram-design/editorial-01-master-cross-functional-handoff--diagramdesign.html) · [SVG](images/svg/editorial-01-master-cross-functional-handoff--diagramdesign.svg)

### Campaign anatomy: each level has one job

**Tree** — parent→children containment. One campaign owns objective and budget; ad sets own targeting and bids; ads own the creative and the click-through URL.

![Campaign anatomy: each level has one job](images/svg/editorial-02-campaign-anatomy--diagramdesign.svg)

**Files:** [`02-campaign-anatomy--diagramdesign.html`](sources/diagram-design/editorial-02-campaign-anatomy--diagramdesign.html) · [SVG](images/svg/editorial-02-campaign-anatomy--diagramdesign.svg)

### The click as messages between five actors

**Sequence** — time flows top→down and the story is who says what to whom: click, redirect+gclid, landing, cookie write, convert, event+click ID.

![The click as messages between five actors](images/svg/editorial-03-click-to-conversion-messages--diagramdesign.svg)

**Files:** [`03-click-to-conversion-messages--diagramdesign.html`](sources/diagram-design/editorial-03-click-to-conversion-messages--diagramdesign.html) · [SVG](images/svg/editorial-03-click-to-conversion-messages--diagramdesign.svg)

### Six seconds inside the click

**Timeline** — the dominant axis is elapsed time (T+0ms → T+days), so events sit on an honest time axis with alternating labels.

![Six seconds inside the click](images/svg/editorial-04-click-journey-timeline--diagramdesign.svg)

**Files:** [`04-click-journey-timeline--diagramdesign.html`](sources/diagram-design/editorial-04-click-journey-timeline--diagramdesign.html) · [SVG](images/svg/editorial-04-click-journey-timeline--diagramdesign.svg)

### How the algorithm learns from every conversion

**Loop** — a reinforcing cycle with a shared hub. Solid ring = work advances clockwise; dashed spokes = each pass writes back to the model state. This is the marquee diagram.

![How the algorithm learns from every conversion](images/svg/editorial-05-algorithm-learning-loop--diagramdesign.svg)

**Files:** [`05-algorithm-learning-loop--diagramdesign.html`](sources/diagram-design/editorial-05-algorithm-learning-loop--diagramdesign.html) · [SVG](images/svg/editorial-05-algorithm-learning-loop--diagramdesign.svg)

### Where the click ID actually lives

**Layer stack** — three stacked abstraction levels (URL parameter → first-party cookie → platform backend), because the point is hierarchy of durability, not sequence.

![Where the click ID actually lives](images/svg/editorial-06-where-click-id-lives--diagramdesign.svg)

**Files:** [`06-where-click-id-lives--diagramdesign.html`](sources/diagram-design/editorial-06-where-click-id-lives--diagramdesign.html) · [SVG](images/svg/editorial-06-where-click-id-lives--diagramdesign.svg)

### Tag architecture: what runs where

**Architecture** — components and connections, grouped by trust boundary (user browser → platform server).

![Tag architecture: what runs where](images/svg/editorial-07-tag-architecture--diagramdesign.svg)

**Files:** [`07-tag-architecture--diagramdesign.html`](sources/diagram-design/editorial-07-tag-architecture--diagramdesign.html) · [SVG](images/svg/editorial-07-tag-architecture--diagramdesign.svg)

### How a conversion gets credited

**Flowchart** — decision gates with branches. Coral is the single happy path; every other branch is a reason the number in Ads Manager is wrong.

![How a conversion gets credited](images/svg/editorial-08-attribution-decision-flow--diagramdesign.svg)

**Files:** [`08-attribution-decision-flow--diagramdesign.html`](sources/diagram-design/editorial-08-attribution-decision-flow--diagramdesign.html) · [SVG](images/svg/editorial-08-attribution-decision-flow--diagramdesign.svg)

## Validation

Each file was checked against the skill's own gates before being committed:

- `skills/diagram-design/scripts/self_check.py` — **8/8 OK** (accessible-SVG contract:
  `role="img"`, resolving `aria-labelledby`, first-child `<title>` + `<desc>`, prefixed IDs;
  single-file safety: no remote assets beyond the Google Fonts stylesheet, no scripts)
- `scripts/verify-geometry.py` — **8 files, 0 findings** (no arrow-label mask clipped by a
  node painted after it — the exact defect class filed in [#1](https://github.com/Rajeev-SG/ad-pixel-conversion-tracking-diagrams/issues/1))
- Rendered in headless Chrome and pixel-checked: no ink touches the canvas edge in any of
  the 8, and every text node sits inside its `viewBox`
- Connector rules enforced in the generator: orthogonal elbows with `r=8`, arrows drawn
  before boxes, every arrow label on an opaque paper mask with a ≥6px gap, fan-out attach
  points ≥12px apart, no diagonal connectors (except the Loop type's documented
  circular-arc ring and radial spokes)

To open one: double-click the `.html` — it is a single self-contained file (only Google
Fonts is fetched over the network; it renders offline with fallback faces).


---

# Sources & citations

Every mechanism above is grounded in official documentation — see [`docs/sources-and-citations.md`](docs/sources-and-citations.md).


## How to edit the diagrams

- **Excalidraw:** open any `sources/excalidraw/*.excalidraw` in [Excalidraw](https://excalidraw.com) (or the local canvas at `http://127.0.0.1:3010`).

- **draw.io:** open `sources/drawio/standard-01-to-07-ad-tracking-diagram-set.drawio` in [diagrams.net](https://app.diagrams.net) — 7 pages, one per standard diagram.

- **Renders:** SVG/PNG in `images/` are generated from those sources. Regenerate draw.io renders with the `draw.io` CLI (`-x -f svg|png --page-index N`); Excalidraw renders via the canvas `screenshot` command.


## Method note (live examples)

Captured with Playwright driving a real Chromium. The IKEA leg used a **synthetic** `gclid` (`DEMO_GCLID_20260924`) to demonstrate the mechanism without billing an advertiser; the MoneySuperMarket leg used one **real** Google Ads search click (single click, user-authorised). The Guardian leg clicked one **house ad** (no third-party cost). Cookie IDs shown are ephemeral browser-session identifiers, not credentials.
