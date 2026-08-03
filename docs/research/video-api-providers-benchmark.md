# AI Video API Providers Benchmark & Pricing Analysis

## Executive Summary
This document analyzes market options for commercial AI Video Generation APIs to integrate into **AI Creative Studio**.

It reviews pricing models, per-second/per-video costs, output quality, latency, and integration complexity to identify the most cost-effective provider stack for a boot-strapped SaaS.

---

## 1. Provider Comparison & Commercial Pricing (2026 Rates)

| Provider / Platform | Billing Model | Base Cost (Per Second / Per Video) | 5-Second Video Cost | Key Strengths | Limitations / Drawbacks |
|---|---|---|---|---|---|
| **Fal.ai** *(Aggregator - Recommended)* | Prepaid Credits / Pay-As-You-Go per second | • **Wan 2.5**: ~$0.05/sec<br>• **Kling 2.5 Turbo**: ~$0.07/sec<br>• **HunyuanVideo**: ~$0.40/video (flat rate)<br>• **Veo 3**: ~$0.40/sec | **~$0.25** (Wan 2.5)<br>**~$0.35** (Kling 2.5)<br>**~$0.40** (Hunyuan) | • Unified Python/JS SDK.<br>• Ultra-fast inference infrastructure.<br>• Instant access to multiple models under 1 billing account. | Includes slight infrastructure margin over raw self-hosted GPU. |
| **RunwayML API** *(Direct)* | Developer Portal Credits ($0.01 / credit) | • **Gen-3 Alpha Turbo**: 5 credits/sec ($0.05/sec)<br>• **Gen-3 Alpha**: 10 credits/sec ($0.10/sec) | **~$0.25** (Turbo)<br>**~$0.50** (Standard) | • Premium cinematic UGC output.<br>• Well-known industry benchmark. | Requires developer portal setup; 100-credit minimum batches. |
| **MiniMax / Hailuo API** *(Direct / Fal)* | Video Points / Pay-As-You-Go | • **Hailuo-2.3-Fast**: 0.7 – 1.3 points per 6s clip (~$0.15–$0.25)<br>• **Hailuo H3 (2K)**: ~$0.13/sec | **~$0.15 – $0.25** (6s clip)<br>**~$0.65** (H3 2K 5s) | • Best human motion & realistic UGC dynamics.<br>• Low cost per 6-second clip. | Asian API endpoint latency can vary; complex point packages. |
| **Replicate** *(Aggregator)* | GPU Runtime per second (H100 / L40S) | • **LTX-Video / SVD**: ~$0.0014/sec GPU time (~$0.05–$0.12/video) | **~$0.08 – $0.15** | • Pay purely for GPU execution.<br>• Open-source models supported. | Self-tuning required for consistent UGC prompt compliance. |
| **Luma Dream Machine** *(Direct)* | Per-clip API rate | • **Ray 2**: ~$0.95 per 5s 1080p clip<br>• **Ray 3 (HDR)**: ~$1.90 per 5s clip | **~$0.95 – $1.90** | High physical realism & camera control. | Most expensive among options; non-transferable consumer credits. |

---

## 2. High-Converting UGC Ad Standards (Length, Aspect Ratio & Structure)

To convert emerging D2C brand visitors into customers on TikTok, Instagram Reels, and YouTube Shorts:

*   **Optimal Duration**: **15 – 30 seconds** (sweet spot for mobile feed retention; 15s for Instagram Reels, 21–34s for narrative TikToks).
*   **Aspect Ratio**: **9:16 vertical (1080 x 1920 px @ 30fps)** mandatory.
*   **High-Converting 4-Scene UGC Structure**:
    1.  **Scene 1: Hook (0–3s)**: High-impact visual + relatable pain point / contrarian statement.
    2.  **Scene 2: Problem & Proof (3–8s)**: Agitate the problem and show struggle or initial transformation.
    3.  **Scene 3: Solution & Product Demo (8–20s)**: Product demo, unboxing, or feature highlight from Brand Brain context.
    4.  **Scene 4: Call to Action / Offer (20–30s)**: Direct CTA ("Get 20% Off - Tap Below").

---

## 3. Unit Economics for Full 15-Second & 30-Second UGC Video Ads

A 15s–30s UGC video is typically created by generating **3 to 6 video shot clips** (each 3s–6s long) and stitching them with captions, voiceovers, and transitions.

| Provider / Model | Cost per 5s Clip | 15-Second UGC Ad Cost (3 Clips) | 30-Second UGC Ad Cost (6 Clips) | Backend Cost vs User Credit Selling Price |
|---|---|---|---|---|
| **Wan 2.5** (via Fal.ai @ $0.05/s) | $0.25 | **$0.75** | **$1.50** | • **15s Ad (3 Credits)**: Cost $0.75 → Retail $2.25 – $3.00 (**75% Margin**)<br>• **30s Ad (6 Credits)**: Cost $1.50 → Retail $4.50 – $6.00 (**75% Margin**) |
| **MiniMax Hailuo Fast** (@ $0.035/s) | $0.18 | **$0.54** | **$1.08** | • **15s Ad (3 Credits)**: Cost $0.54 → Retail $2.25 (**76% Margin**)<br>• **30s Ad (6 Credits)**: Cost $1.08 → Retail $4.50 (**76% Margin**) |
| **Kling 2.5 Turbo** (via Fal.ai @ $0.07/s) | $0.35 | **$1.05** | **$2.10** | • **15s Ad (3 Credits)**: Cost $1.05 → Retail $2.50 (**58% Margin**)<br>• **30s Ad (6 Credits)**: Cost $2.10 → Retail $5.00 (**58% Margin**) |
| **Runway Gen-3 Alpha Turbo** (@ $0.05/s) | $0.25 | **$0.75** | **$1.50** | • **15s Ad (3 Credits)**: Cost $0.75 → Retail $2.25 (**75% Margin**) |

---

## 4. Recommended Provider Roadmap for MVP

### Phase 1 (Initial Build & Mock Testing):
- Use the **Mock Backend Provider Adapter** (already defined in [mvp-technical-spec.md](../mvp-technical-spec.md)).
- Zero GPU cost during early UI/API development.

### Phase 2 (Live Provider Integration):
- **Primary Provider**: **Fal.ai**
  - **Models**:
    1. **Wan 2.5** ($0.05/sec) for fast, low-cost draft & standard UGC variations.
    2. **MiniMax Hailuo** ($0.035–$0.04/sec) or **Kling 2.5 Turbo** ($0.07/sec) for realistic human UGC ads.
- **Why Fal.ai is the ideal choice for a solo founder**:
  1. No monthly API commit or enterprise minimums (pay only for generated seconds).
  2. Single backend adapter in FastAPI can switch between Wan 2.5, Kling, and Hunyuan by changing a single parameter (`model_id`), avoiding vendor lock-in.
