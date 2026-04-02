<script setup>
import { ref, onMounted } from 'vue'

const slides = [
  'https://floodrestorationgeelong.au/wp-content/uploads/2026/01/flood-restoration-geelong-van-residential-property-equipment.webp',
  'https://floodrestorationgeelong.au/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-10-at-2.16.37-PM.webp',
  'https://floodrestorationgeelong.au/wp-content/uploads/2025/10/Carpet-cleaning-2-1-1.webp'
]

const currentSlide = ref(0)

onMounted(() => {
  setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
})
</script>

<template>
  <section class="hero">
    <div class="slideshow">
      <div 
        v-for="(slide, index) in slides" 
        :key="index"
        class="slide"
        :class="{ active: currentSlide === index }"
        :style="{ backgroundImage: `url(${slide})` }"
      ></div>
      <div class="overlay"></div>
    </div>

    <div class="container hero-content">
      <div class="section-label" style="color: var(--blue-light)">Geelong Flood Restoration</div>
      <h1 class="hero-title">Geelong's #1 Flood Restoration & Water Damage Repair Experts</h1>
      <p class="hero-description">
        Emergency <strong>Water Damage Repairs Geelong</strong> | <strong>24/7 Flood Recovery</strong> – 
        Flood Restoration Geelong offers around-the-clock emergency water damage repairs in Geelong. 
        Our <strong>IICRC-certified team</strong> with over 20 years of experience provides rapid water extraction, drying, and recovery.
      </p>
      
      <div class="hero-btns">
        <a href="tel:0459338998" class="btn btn-emergency">
          <span class="icon">📞</span> Call Now 0459 338 998
        </a>
        <a href="#contact" class="btn btn-outline">Get a Free Quote</a>
      </div>

      <div class="hero-badges">
        <div class="badge">✔ IICRC Certified</div>
        <div class="badge">✔ 20+ Years Experience</div>
        <div class="badge">✔ Available 24/7</div>
        <div class="badge">✔ Insurance Assist</div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  position: relative;
  min-height: calc(100vh - 100px); /* Adjust for header/topbar */
  display: flex;
  align-items: center;
  color: var(--white);
  padding: 100px 0;
  overflow: hidden;
}

.slideshow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: opacity 1.5s ease-in-out;
}

.slide.active {
  opacity: 1;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(7, 26, 48, 0.85), rgba(0, 119, 200, 0.45));
}

.hero-content {
  max-width: 850px;
  text-align: left;
}

.hero-title {
  font-size: clamp(32px, 6vw, 64px);
  line-height: 1.1;
  margin-bottom: 24px;
  color: var(--white);
  font-weight: 800;
}

.hero-description {
  font-size: clamp(16px, 2vw, 19px);
  margin-bottom: 40px;
  max-width: 700px;
  opacity: 0.95;
  color: var(--white);
}

.hero-btns {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 40px;
}

.hero-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.badge {
  background: rgba(255, 255, 255, 0.10);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: rgba(255, 255, 255, 0.9);
  font-size: 13px;
  font-weight: 600;
  padding: 8px 14px;
  border-radius: 6px;
}

@media (max-width: 768px) {
  .hero {
    min-height: auto;
    text-align: center;
    padding: 80px 0;
  }
  
  .hero-content {
    text-align: center;
  }
  
  .hero-btns, .hero-badges {
    justify-content: center;
  }
}
</style>
