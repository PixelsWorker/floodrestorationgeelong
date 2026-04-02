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
          We are not a call centre or a franchise sending technicians from outside the region. We are a 
          locally based Geelong business, serving homeowners, landlords, real estate 
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

        <a href="https://floodrestorationgeelong.au/our-works" target="_blank" rel="noopener" class="btn btn-primary">OUR FLOOD RESTORATION WORK GALLERY</a>
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
  padding: 100px 0;
}

.grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 80px;
  align-items: center;
}

h2 {
  font-size: 36px;
  color: var(--navy);
  margin-bottom: 30px;
}

p {
  color: var(--text-mid);
  margin-bottom: 25px;
  font-size: 16.5px;
  line-height: 1.8;
}

.benefits {
  background-color: var(--bg-accent);
  padding: 40px;
  border-radius: 12px;
  margin: 35px 0;
  border: 1px solid rgba(0, 119, 204, 0.08);
}

.benefits h3 {
  font-size: 19px;
  margin-bottom: 20px;
  color: var(--navy);
}

.benefits ul {
  display: grid;
  grid-template-columns: 1fr;
  gap: 15px;
}

.benefits li {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 600;
  font-size: 15px;
  color: var(--navy);
}

.btn-primary {
  padding: 18px 35px;
  font-size: 14px;
  letter-spacing: 1px;
}

.image-box img {
  border-radius: 15px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
  width: 100%;
}

@media (max-width: 992px) {
  .grid {
    grid-template-columns: 1fr;
    gap: 50px;
  }
  
  .image-box {
    order: -1;
  }
}
</style>
