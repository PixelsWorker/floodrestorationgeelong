<template>
  <section class="emergency-banner">
    <div class="container banner-inner">
      <div class="banner-text">
        <h2>Has Your Property Been Affected by Water Damage?</h2>
        <p>Expert 24/7 assistance is just a phone call away. Don't wait for mould to grow.</p>
      </div>
      <div class="banner-cta">
        <a href="tel:0459338998" class="btn btn-outline btn-large">
          <span class="icon">📞</span> Call 0459 338 998 Now
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.emergency-banner {
  background: linear-gradient(rgba(30, 96, 227, 0.85), rgba(227, 30, 36, 0.85)), url('https://floodrestorationgeelong.au/wp-content/uploads/2026/01/commercial-flood-recovery-in-progress-geelong.webp');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: var(--white);
  padding: 80px 0;
}

.banner-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 30px;
}

.banner-text h2 {
  font-size: 32px;
  margin-bottom: 12px;
  line-height: 1.2;
}

.banner-text p {
  opacity: 0.95;
  font-size: 19px;
  max-width: 600px;
}

.btn-large {
  padding: 18px 40px;
  font-size: 20px;
  font-weight: 700;
}

@media (max-width: 992px) {
  .banner-inner {
    flex-direction: column;
    text-align: center;
    gap: 40px;
  }
  
  .banner-text h2 {
    font-size: 28px;
  }
}
</style>
