<script setup>
import { inject } from 'vue'
const openQuoteModal = inject('openQuoteModal')
</script>

<template>
  <section class="emergency-banner">
    <div class="banner-bg-container">
      <img 
        src="https://floodrestorationgeelong.au/wp-content/uploads/2026/01/commercial-flood-recovery-in-progress-geelong.webp" 
        alt="Commercial Flood Recovery" 
        class="banner-bg-img"
        loading="lazy"
        decoding="async"
        width="1920"
        height="600"
      />
    </div>
    <div class="banner-overlay"></div>
    <div class="container banner-inner">
      <div class="banner-text">
        <label class="emergency-tag">Available 24/7</label>
        <h2>Has Your Property Been Affected by Water Damage?</h2>
        <p>Expert restoration assistance is just a phone call away. Don't let water damage lead to permanent mould growth.</p>
      </div>
      <div class="banner-cta">
        <div class="cta-flex">
          <a href="tel:0459338998" class="btn btn-emergency btn-pulse btn-large">
            <span class="icon">📞</span> Call 0459 338 998 Now
          </a>
          <button class="btn btn-outline-white btn-large" @click="openQuoteModal">
            Get an Estimate
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.emergency-banner {
  position: relative;
  background-color: var(--navy);
  color: var(--white);
  padding: 100px 0;
  overflow: hidden;
}

.banner-bg-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.banner-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cta-flex {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 100%;
}

.btn-outline-white {
  background: transparent;
  border: 2px solid var(--white);
  color: var(--white);
}
.btn-outline-white:hover {
  background: var(--white);
  color: var(--navy);
}

.banner-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(27, 50, 82, 0.95) 0%, rgba(227, 30, 36, 0.4) 100%);
  z-index: 1;
}

.banner-inner {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 40px;
}

.emergency-tag {
  display: inline-block;
  background: var(--red);
  color: var(--white);
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 15px;
}

.banner-text h2 {
  font-size: clamp(28px, 4vw, 40px);
  margin-bottom: 16px;
  line-height: 1.2;
  color: var(--white);
}

.banner-text p {
  opacity: 0.9;
  font-size: 20px;
  max-width: 650px;
  line-height: 1.6;
}

.btn-large {
  padding: 22px 50px;
  font-size: 22px;
  font-weight: 800;
  border: none;
}

.btn-pulse {
  animation: pulse 2s infinite;
  box-shadow: 0 0 0 0 rgba(227, 30, 36, 0.7);
}

@keyframes pulse {
  0% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(227, 30, 36, 0.7);
  }
  70% {
    transform: scale(1.05);
    box-shadow: 0 0 0 20px rgba(227, 30, 36, 0);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(227, 30, 36, 0);
  }
}

@media (max-width: 992px) {
  .banner-inner {
    flex-direction: column;
    text-align: center;
    gap: 30px;
  }
  
  .banner-text p {
    margin: 0 auto;
    font-size: 18px;
  }
  
  .emergency-banner {
    padding: 70px 0;
  }
}

@media (max-width: 600px) {
  .emergency-banner {
    padding: 60px 0;
  }
  .btn-large {
    padding: 18px 30px;
    font-size: 18px;
    width: 100%;
  }
  .banner-text h2 {
    font-size: 26px;
  }
}

</style>

