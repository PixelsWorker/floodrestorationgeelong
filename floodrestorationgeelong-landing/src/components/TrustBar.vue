<template>
  <section class="trust-bar">
    <div class="container trust-inner">
      <div class="trust-content">
        <div class="section-label" style="color: var(--blue-light)">24/7 Expert Response</div>
        <h3 class="section-title">Fast, Reliable Emergency Service</h3>
        <p class="section-subtitle">
          At <strong>Flood Restoration Geelong</strong>, we deliver fast, reliable, and 
          <strong>professional 24/7 emergency flood and water damage restoration services</strong>. 
          With over 20 years of hands-on experience, our <strong>IICRC-certified technicians</strong> 
          are known for restoring properties quickly, safely, and efficiently.
        </p>
        <div class="badges">
          <div class="badge">
            <span class="icon trust-icon">✅</span>
            <span>IICRC Certified</span>
          </div>
          <div class="badge">
            <span class="icon trust-icon">⏰</span>
            <span>24/7 Service</span>
          </div>
          <div class="badge">
            <span class="icon trust-icon">🏠</span>
            <span>Local Geelong Team</span>
          </div>
        </div>
      </div>
      <div class="trust-image">
        <img 
          src="https://floodrestorationgeelong.au/wp-content/uploads/2026/01/flood-restoration-geelong-van-with-equipment-768x1024.webp" 
          alt="Flood Restoration Geelong Emergency Response Van"
        />
      </div>
    </div>
  </section>
</template>

<style scoped>
.trust-bar {
  background-color: var(--navy);
  padding: 80px 0;
  color: var(--white);
}

.trust-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.section-title {
  color: var(--white);
  margin-bottom: 24px;
}

.section-subtitle {
  color: rgba(255, 255, 255, 0.85);
  margin-bottom: 40px;
  font-size: 17px;
}

.section-subtitle strong {
  color: var(--white);
}

.badges {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

.badge {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: rgba(255, 255, 255, 0.08); /* Semi-transparent white */
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 12px 22px;
  border-radius: 50px;
  font-weight: 600;
  color: var(--white);
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
}

.trust-icon {
  color: var(--blue-light);
  font-size: 16px;
}

.trust-image img {
  border-radius: 12px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.35);
  max-width: 100%;
}

@media (max-width: 992px) {
  .trust-inner {
    grid-template-columns: 1fr;
    gap: 40px;
    text-align: center;
  }
  
  .badges {
    justify-content: center;
  }
  
  .trust-image {
    order: -1;
    max-width: 600px;
    margin: 0 auto;
  }
}
</style>
