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
      <h1>Flood Restoration Geelong</h1>
      <h2>Geelong's #1 Flood Restoration & Water Damage Repair Experts</h2>
      <p>
        Emergency <strong>Water Damage Repairs Geelong</strong> | <strong>24/7 Flood Recovery</strong> – 
        Flood Restoration Geelong offers around-the-clock emergency water damage repairs in Geelong. 
        Our <strong>IICRC-certified team</strong> with over 20 years of experience provides rapid water extraction, drying, and recovery.
      </p>
      <div class="hero-btns">
        <a href="tel:0459338998" class="btn btn-emergency">
          <span class="icon">📞</span> Call us 0459 338 998
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  color: var(--white);
  padding-top: 100px;
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
  background: linear-gradient(rgba(11, 37, 69, 0.7), rgba(11, 37, 69, 0.5));
}

.hero-content {
  max-width: 800px;
  text-align: left;
}

h1 {
  font-size: 18px;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 20px;
  color: var(--primary-hover);
}

h2 {
  font-size: 48px;
  line-height: 1.2;
  margin-bottom: 24px;
}

p {
  font-size: 18px;
  margin-bottom: 35px;
  max-width: 600px;
}

.btn-emergency {
  font-size: 18px;
  padding: 15px 35px;
  background-color: #e31e24; /* Red for emergency */
}

.btn-emergency:hover {
  background-color: #c4191e;
}

@media (max-width: 768px) {
  h2 {
    font-size: 32px;
  }
}
</style>
