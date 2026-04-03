<script setup>
import { ref, onMounted, inject } from 'vue'

const openQuoteModal = inject('openQuoteModal')

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
      <div class="content-left">
        <label class="section-label" style="color: var(--blue-light); margin-bottom: 20px;">Flood Restoration Geelong</label>
        <h1 class="hero-title">Geelong's #1 Flood Restoration & Water Damage Repair Experts</h1>
        <p class="hero-description">
          Emergency <strong>Water Damage Repairs Geelong</strong> | <strong>24/7 Flood Recovery</strong> – 
          Flood Restoration Geelong offers around-the-clock emergency water damage repairs in Geelong. 
          Our <strong>IICRC-certified team</strong> with over 20 years of experience provides rapid water extraction, drying, and recovery.
        </p>
        
        <div class="hero-btns">
          <a href="tel:0459338998" class="btn btn-emergency">
            <span class="icon">📞</span> CALL US 0459 338 998
          </a>
          <a href="#" class="btn btn-outline" @click.prevent="openQuoteModal">Get a Quote</a>
        </div>

        <div class="hero-badges">
          <div class="badge">✔ IICRC Certified</div>
          <div class="badge">✔ 20+ Years Experience</div>
          <div class="badge">✔ Available 24/7</div>
          <div class="badge">✔ Insurance Assist</div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  position: relative;
  min-height: 85vh;
  display: flex;
  align-items: center;
  color: var(--white);
  padding: 120px 0;
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
  background: linear-gradient(90deg, rgba(7, 26, 48, 0.95) 0%, rgba(7, 26, 48, 0.65) 60%, rgba(7, 26, 48, 0.45) 100%);
}

.content-left {
  max-width: 850px;
  text-align: left;
}

  .hero-title {
  font-size: clamp(26px, 7vw, 56px);
  line-height: 1.15;
  margin-bottom: 24px;
  color: var(--white);
  font-weight: 800;
  letter-spacing: -0.5px;
}

.hero-description {
  font-size: clamp(15px, 2vw, 19px);
  margin-bottom: 35px;
  max-width: 750px;
  opacity: 0.95;
  color: var(--white);
  line-height: 1.6;
}

.hero-btns {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 35px;
}

.btn-emergency {
  padding: 16px 35px;
  font-size: 17px;
  box-shadow: 0 10px 20px rgba(227, 30, 36, 0.3);
}

.hero-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.badge {
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: rgba(255, 255, 255, 0.95);
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 50px;
}

@media (max-width: 992px) {
  .hero {
    min-height: auto;
    padding: 80px 0;
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 60px 0 80px;
  }

  .content-left {
    text-align: center;
  }
  
  .hero-btns, .hero-badges {
    justify-content: center;
  }
  
  .hero-btns {
    flex-direction: column;
    width: 100%;
    max-width: 400px;
    margin: 0 auto 35px;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }
  
  .hero-title {
    margin-bottom: 20px;
  }
  
  .hero-description {
    margin-bottom: 30px;
  }
}

</style>
