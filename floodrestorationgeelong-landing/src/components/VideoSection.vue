<script setup>
import { ref } from 'vue'

const videos = ref([
  {
    id: '3MpcsgzQGE0',
    title: 'Flood Restoration in Office',
    playing: false
  },
  {
    id: 'ub6Bk-nlje8',
    title: 'Water Damage Restoration',
    playing: false
  },
  {
    id: 'ZOd4APGKdH0',
    title: 'Flood Damage Restoration',
    playing: false
  },
  {
    id: 'p2jKh8yj160',
    title: 'Emergency Water Damage',
    playing: false
  }
])
</script>

<template>
  <section class="video-showcase">
    <div class="container">
      <div class="section-header">
        <label class="section-label">Video Gallery</label>
        <h2 class="section-title">See Our Restoration Team in Action</h2>
        <p class="section-subtitle">Real results from real flood emergencies across Geelong properties.</p>
      </div>

      <div class="video-grid">
        <div v-for="video in videos" :key="video.id" class="video-card">
          <div class="video-wrapper">
            <div v-if="!video.playing" class="video-facade" @click="video.playing = true">
              <img 
                :src="`https://img.youtube.com/vi/${video.id}/hqdefault.jpg`" 
                :alt="video.title" 
                class="video-thumb"
              />
              <div class="play-button">
                <svg viewBox="0 0 140 140" width="60"><circle cx="70" cy="70" r="65" fill="rgba(0,0,0,0.5)"/><polygon points="50,40 100,70 50,100" fill="white"/></svg>
              </div>
            </div>
            <iframe 
              v-else
              :src="`https://www.youtube-nocookie.com/embed/${video.id}?autoplay=1`" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowfullscreen
            ></iframe>
          </div>
          <div class="video-info">
            <h3>{{ video.title }}</h3>
          </div>
        </div>
      </div>
      <div class="video-cta">
        <a href="https://floodrestorationgeelong.au/our-works" target="_blank" rel="noopener" class="btn btn-primary highlight-btn">
          OUR FLOOD RESTORATION WORK GALLERY
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.video-showcase {
  background-color: var(--white);
}

.video-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
}

.video-card {
  background: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-card);
  transition: var(--transition-fast);
}

.video-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-main);
}

.video-wrapper {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
}

.video-wrapper iframe, .video-facade {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.video-facade {
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #000;
}

.video-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.8;
  transition: opacity 0.3s;
}

.video-facade:hover .video-thumb {
  opacity: 1;
}

.play-button {
  position: absolute;
  z-index: 2;
  transition: transform 0.3s;
}

.video-facade:hover .play-button {
  transform: scale(1.1);
}

.video-info {
  padding: 20px;
  text-align: center;
}

.video-info h3 {
  font-size: 18px;
  color: var(--navy);
}

@media (max-width: 768px) {
  .video-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .video-showcase {
    padding: 60px 0;
  }
}

.video-cta {
  margin-top: 50px;
  display: flex;
  justify-content: center;
}

.highlight-btn {
  padding: 20px 45px;
  font-size: 16px;
  background: var(--navy);
  border-color: var(--navy);
  box-shadow: 0 10px 20px rgba(27, 50, 82, 0.15);
}

.highlight-btn:hover {
  background: var(--blue);
  border-color: var(--blue);
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 30px rgba(0, 124, 190, 0.25);
}

.btn-icon {
  margin-left: 10px;
  transition: transform 0.3s;
}

.highlight-btn:hover .btn-icon {
  transform: translateX(5px);
}
</style>
