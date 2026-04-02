<template>
  <section class="why-choose-us">
    <div class="container grid">
      <div class="content">
        <h2>Our Approach to Flood Damage Restoration in Geelong</h2>
        <p>
          At <strong>Flood Restoration Geelong</strong>, we understand the devastating impact 
          that a flood or major water leak can have. It’s more than just property damage; 
          it’s emotional stress and disruption to your daily life.
        </p>
        <p>
          We are a locally based Geelong business, serving homeowners, landlords, real estate 
          agencies, and commercial premises across <strong>Geelong and surrounding suburbs</strong>.
        </p>
        
        <div class="benefits">
          <h3>Because we’re local, we understand:</h3>
          <ul>
            <li><span>🔹</span> Geelong’s weather patterns and storm risks</li>
            <li><span>🔹</span> Older plumbing systems common in established suburbs</li>
            <li><span>🔹</span> Coastal humidity and its impact on mould growth</li>
            <li><span>🔹</span> Local building materials and construction methods</li>
          </ul>
        </div>

        <a href="/our-works" class="btn btn-outline">Our Work Gallery</a>
      </div>
      <div class="image-box">
        <img 
          src="https://floodrestorationgeelong.au/wp-content/uploads/2026/01/mould-removal-geelong-residential-property.jpg" 
          alt="Local Geelong Restoration Service"
        />
      </div>
    </div>
  </section>
</template>

<style scoped>
.why-choose-us {
  background-color: var(--white);
}

.grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 80px;
  align-items: center;
}

h2 {
  font-size: 32px;
  color: var(--secondary-color);
  margin-bottom: 25px;
}

p {
  color: var(--text-light);
  margin-bottom: 20px;
  font-size: 16px;
}

.benefits {
  background-color: var(--bg-accent);
  padding: 30px;
  border-radius: 12px;
  margin: 30px 0;
}

.benefits h3 {
  font-size: 18px;
  margin-bottom: 15px;
  color: var(--secondary-color);
}

.benefits ul {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

.benefits li {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 500;
  font-size: 14px;
}

.btn-outline {
  background-color: transparent;
  border: 2px solid var(--primary-color);
  color: var(--primary-color);
}

.btn-outline:hover {
  background-color: var(--primary-color);
  color: var(--white);
}

.image-box img {
  border-radius: 12px;
  box-shadow: var(--shadow-main);
}

@media (max-width: 992px) {
  .grid {
    grid-template-columns: 1fr;
    gap: 50px;
  }
  
  .benefits ul {
    grid-template-columns: 1fr;
  }
}
</style>
