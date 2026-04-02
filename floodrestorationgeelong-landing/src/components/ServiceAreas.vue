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
      <div class="section-title">
        <h2>Area We Service</h2>
        <p>Providing rapid flood restoration across Geelong and surroundings.</p>
      </div>

      <div class="suburbs-grid">
        <ul v-for="col in 4" :key="col">
          <li v-for="(suburb, index) in suburbs.slice((col-1)*13, col*13)" :key="index">
            <span class="dot">📍</span> {{ suburb }}
          </li>
        </ul>
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
}

.section-title {
  text-align: center;
  margin-bottom: 40px;
}

.suburbs-grid {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 50px;
  flex-wrap: wrap;
}

.suburbs-grid ul {
  flex: 1;
  min-width: 200px;
}

.suburbs-grid li {
  padding: 8px 0;
  border-bottom: 1px solid #f0f0f0;
  font-size: 14px;
  color: var(--text-light);
  display: flex;
  align-items: center;
  gap: 10px;
}

.dot {
  font-size: 12px;
}

.map-container {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-main);
  margin-top: 40px;
}

@media (max-width: 768px) {
  .suburbs-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
</style>
