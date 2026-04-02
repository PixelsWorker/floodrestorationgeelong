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
        <label class="section-label" style="color: var(--blue-light)">Service Coverage</label>
        <h2 class="section-title">Area We Service</h2>
        <p class="section-subtitle">Providing rapid flood restoration across Geelong and surroundings.</p>
      </div>

      <div class="suburbs-grid">
        <div v-for="col in 4" :key="col" class="suburb-col">
          <ul class="suburb-list">
            <li v-for="(suburb, index) in suburbs.slice((col-1)*13, col*13)" :key="index">
              <span class="area-tag">📍 {{ suburb }}</span>
            </li>
          </ul>
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
  background-color: var(--navy);
  padding: 80px 0;
}

.section-title {
  color: var(--white);
}

.section-subtitle {
  color: rgba(255, 255, 255, 0.9);
  margin: 0 auto 56px;
}

.suburbs-grid {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 50px;
  flex-wrap: wrap;
}

.suburb-col {
  flex: 1;
  min-width: 180px;
}

.suburb-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.area-tag {
  display: inline-block;
  background: rgba(255, 255, 255, 0.08); /* Semi-transparent */
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: rgba(255, 255, 255, 0.85);
  padding: 8px 16px;
  border-radius: 100px;
  font-size: clamp(12px, 1.5vw, 14px);
  cursor: pointer;
  transition: var(--transition-fast);
  white-space: nowrap;
}

.area-tag:hover {
  background: var(--blue);
  border-color: var(--blue);
  color: white;
  transform: translateY(-2px);
}

.map-container {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
  margin-top: 40px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

@media (max-width: 992px) {
  .suburbs-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }
}

@media (max-width: 576px) {
  .suburbs-grid {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .suburb-list {
    align-items: center;
  }
}
</style>
