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
      >
        <img 
          :src="slide" 
          alt="Flood Restoration Geelong" 
          :fetchpriority="index === 0 ? 'high' : 'auto'"
          :decoding="index === 0 ? 'sync' : 'async'"
          width="1920"
          height="1080"
          class="hero-img"
        />
      </div>
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
          <div class="badge"><span class="check">✔</span> IICRC Certified</div>
          <div class="badge"><span class="check">✔</span> 20+ Years Experience</div>
          <div class="badge"><span class="check">✔</span> Available 24/7</div>
          <div class="badge"><span class="check">✔</span> Insurance Assist</div>
        </div>

        <div class="hero-urgency">
          <span class="pulse-icon">⚡</span> 
          <span>Geelong Technicians On-Site Within <strong>60 Minutes</strong></span>
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
  opacity: 0;
  transition: opacity 1.5s ease-in-out;
}

.hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  background: rgba(0, 124, 190, 0.25);
  border: 1.5px solid rgba(0, 163, 224, 0.6);
  color: #ffffff;
  font-size: 14px;
  font-weight: 800;
  padding: 10px 20px;
  border-radius: 50px;
  letter-spacing: 0.3px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.check {
  color: #2ecc71;
  font-size: 18px;
}

.hero-urgency {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  margin-top: 25px;
  padding: 12px 24px;
  background: rgba(21, 255, 0, 0.136);
  border: 1px solid rgba(0, 255, 51, 0.4);
  border-radius: 50px;
  font-size: 16px;
  color: #ffffff;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  animation: pulse-glow 2.5s infinite;
}

.hero-urgency strong {
  font-weight: 800;
  letter-spacing: 0.5px;
}

.pulse-icon {
  font-size: 20px;
  animation: bounce-slight 2s infinite;
}

@keyframes pulse-glow {
  0% { box-shadow: 0 0 0 0 rgba(145, 255, 0, 0.3); }
  70% { box-shadow: 0 0 0 10px rgba(204, 255, 0, 0); }
  100% { box-shadow: 0 0 0 0 rgba(187, 255, 0, 0); }
}

@keyframes bounce-slight {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-3px); }
}

@media (max-width: 992px) {
  .hero {
    min-height: auto;
    padding: 80px 0;
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 50px 0 60px;
  }

  .content-left {
    text-align: center;
  }
  
  .hero-btns, .hero-badges {
    justify-content: center;
  }

  .hero-urgency {
    font-size: 14px;
    padding: 10px 20px;
    justify-content: center;
    width: 100%;
    max-width: 400px;
    margin: 15px auto 0;
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

  .badge {
    font-size: 14px;
    font-weight: 800;
    padding: 10px 20px;
    border: 2px solid rgba(0, 163, 224, 0.8);
    background: rgba(0, 124, 190, 0.4);
  }
}

</style>
