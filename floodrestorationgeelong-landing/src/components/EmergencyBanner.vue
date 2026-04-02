<template>
  <section class="emergency-banner">
    <div class="container banner-inner">
      <div class="banner-text">
        <h2>Has Your Property Been Affected by Water Damage?</h2>
        <p>Expert 24/7 assistance is just a phone call away. Don't wait for mould to grow.</p>
      </div>
      <div class="banner-cta">
        <a href="tel:0459338998" class="btn btn-large">
          <span class="icon">📞</span> Call 0459 338 998 Now
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.emergency-banner {
  background: linear-gradient(135deg, var(--secondary-color), var(--primary-color));
  color: var(--white);
  padding: 50px 0;
}

.banner-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 30px;
}

.banner-text h2 {
  font-size: 28px;
  margin-bottom: 10px;
}

.banner-text p {
  opacity: 0.9;
  font-size: 18px;
}

.btn-large {
  padding: 18px 40px;
  font-size: 20px;
  background-color: var(--white);
  color: var(--primary-color);
}

.btn-large:hover {
  background-color: var(--bg-accent);
  color: var(--primary-hover);
}

@media (max-width: 768px) {
  .banner-inner {
    flex-direction: column;
    text-align: center;
  }
}
</style>
