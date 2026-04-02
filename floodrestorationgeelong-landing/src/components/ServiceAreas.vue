<script setup>
const suburbs = [
  'Anakie', 'Anglesea', 'Armstrong Creek', 'Bannockburn', 'Barwon Heads', 'Batesford', 'Bellarine', 'Bell Post Hill', 'Belmont', 'Breakwater',
  'Breamlea', 'Ceres', 'Charlemont', 'Clifton Springs', 'Corio', 'Curlewis', 'Drumcondra', 'Drysdale', 'East Geelong', 'Fyansford',
  'Geelong', 'Geelong West', 'Gheringhap', 'Golden Plains', 'Grovedale', 'Hamlyn Heights', 'Herne Hill', 'Highton', 'Lara', 'Leopold',
  'Lethbridge', 'Little River', 'Lovely Banks', 'Marshall', 'Maude', 'Meredith', 'Moolap', 'Mount Duneed', 'Newcomb', 'Newtown',
  'Norlane', 'North Geelong', 'Northshore', 'Ocean Grove', 'Point Lonsdale', 'Portarlington', 'Queenscliff', 'Rippleside', 'She Oaks', 'South Geelong',
  'St Albans Park', 'Stieglitz', 'Sutherlands Creek', 'Torquay', 'Wallington', 'Wandana Heights', 'Waurnponds', 'Whittington'
]
</script>

<template>
  <section class="service-areas">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Area We Service</h2>
        <p class="section-subtitle">Providing rapid flood restoration across Geelong and surroundings.</p>
      </div>

      <div class="suburbs-grid">
        <div v-for="suburb in suburbs" :key="suburb" class="suburb-item">
          <span class="dot">📍</span> {{ suburb }}
        </div>
      </div>

      <div class="map-container">
        <iframe 
          src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d803224.2130031711!2d144.359996!3d-38.149619!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad4141b7a300001%3A0x15a3eb0b8ed8cf39!2sFlood%20Restoration%20Geelong!5e0!3m2!1sen!2sin!4v1759817744441!5m2!1sen!2sin" 
          width="100%" 
          height="450" 
          style="border:0;" 
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade"
        ></iframe>
      </div>
    </div>
  </section>
</template>

<style scoped>
.service-areas {
  background-color: var(--white);
  padding: 100px 0;
}

.suburbs-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px 20px;
  margin-bottom: 60px;
}

.suburb-item {
  font-size: 15px;
  color: var(--blue);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: var(--transition-fast);
  padding: 4px 0;
}

.suburb-item:hover {
  color: var(--navy);
  transform: translateX(3px);
}

.dot {
  font-size: 14px;
  opacity: 0.9;
}

.map-container {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-main);
  border: 1px solid var(--border);
}

@media (max-width: 992px) {
  .suburbs-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .suburbs-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .suburbs-grid {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>
