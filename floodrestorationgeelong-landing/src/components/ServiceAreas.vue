<script setup>
const suburbs = [
  'Belmont', 'Highton', 'Armstrong Creek', 'Charlemont', 'Marshall', 'Corio', 'Leopold', 'Newcomb', 'Waurnponds', 'Moolap',
  'Geelong', 'South Geelong', 'North Geelong', 'Mount Duneed', 'Wallington', 'Gheringhap', 'Breamlea', 'Anglesea', 'Ocean Grove', 'Barwon Heads',
  'Queenscliff', 'Portarlington', 'Point Lonsdale', 'Bellarine', 'Drumcondra', 'Rippleside', 'Curlewis', 'Clifton Springs', 'Lethbridge', 'Drysdale',
  'Ceres', 'Newtown', 'Breakwater', 'Norlane', 'Lovely Banks', 'East Geelong', 'Whittington', 'Torquay', 'Grovedale', 'Geelong West',
  'Wandana Heights', 'Meredith', 'She Oaks', 'Sutherlands Creek', 'Maude', 'Stieglitz', 'Anakie', 'St Albans Park', 'Lara', 'Little River'
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
  grid-template-columns: repeat(6, 1fr);
  gap: 15px;
  margin-bottom: 60px;
}

.suburb-item {
  font-size: 14px;
  color: var(--blue);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: var(--transition-fast);
}

.suburb-item:hover {
  color: var(--navy);
  transform: translateX(3px);
}

.dot {
  font-size: 12px;
  opacity: 0.8;
}

.map-container {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-main);
  border: 1px solid var(--border);
}

@media (max-width: 1200px) {
  .suburbs-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 900px) {
  .suburbs-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 600px) {
  .suburbs-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
