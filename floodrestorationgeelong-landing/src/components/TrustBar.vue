<template>
  <section class="trust-bar">
    <div class="container trust-inner">
      <div class="trust-content">
        <h3>Fast, Reliable 24/7 Emergency Service</h3>
        <p>
          At <strong>Flood Restoration Geelong</strong>, we deliver fast, reliable, and 
          <strong>professional 24/7 emergency flood and water damage restoration services</strong>. 
          With over 20 years of hands-on experience, our <strong>IICRC-certified technicians</strong> 
          are known for restoring properties quickly, safely, and efficiently.
        </p>
        <div class="badges">
          <div class="badge">
            <span class="icon">✅</span>
            <span>IICRC Certified</span>
          </div>
          <div class="badge">
            <span class="icon">⏰</span>
            <span>24/7 Service</span>
          </div>
          <div class="badge">
            <span class="icon">🏠</span>
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
  background-color: var(--bg-accent);
  padding: 60px 0;
}

.trust-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.trust-content h3 {
  font-size: 28px;
  color: var(--secondary-color);
  margin-bottom: 20px;
}

.trust-content p {
  color: var(--text-light);
  margin-bottom: 30px;
  font-size: 16px;
}

.badges {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: var(--white);
  padding: 10px 18px;
  border-radius: 50px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  font-weight: 600;
  color: var(--primary-color);
}

.trust-image img {
  border-radius: 12px;
  box-shadow: var(--shadow-main);
  max-width: 100%;
}

@media (max-width: 768px) {
  .trust-inner {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .trust-image {
    order: -1;
  }
}
</style>
