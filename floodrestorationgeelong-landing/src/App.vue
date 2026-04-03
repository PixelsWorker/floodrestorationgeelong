<script setup>
import { ref, provide } from 'vue'
import SiteHeader from './components/SiteHeader.vue'
import HeroSection from './components/HeroSection.vue'
import ServicesSection from './components/ServicesSection.vue'
import TrustBar from './components/TrustBar.vue'
import HowItWorks from './components/HowItWorks.vue'
import VideoSection from './components/VideoSection.vue'
import EmergencyBanner from './components/EmergencyBanner.vue'
import TestimonialsSection from './components/TestimonialsSection.vue'
import FaqSection from './components/FaqSection.vue'
import ContactSection from './components/ContactSection.vue'
import SiteFooter from './components/SiteFooter.vue'
import QuoteModal from './components/QuoteModal.vue'

const isQuoteModalOpen = ref(false)

const openQuoteModal = () => {
  isQuoteModalOpen.value = true
  document.body.style.overflow = 'hidden' // Lock scroll
}

const closeQuoteModal = () => {
  isQuoteModalOpen.value = false
  document.body.style.overflow = '' // Unlock scroll
}

// Provide to all children
provide('openQuoteModal', openQuoteModal)
</script>

<template>
  <div class="app-wrapper">
    <SiteHeader />
    <main>
      <HeroSection />
      <ServicesSection />
      <TrustBar />
      <HowItWorks />
      <VideoSection />
      <EmergencyBanner />
      <TestimonialsSection />
      <FaqSection />
      <ContactSection />
    </main>
    <SiteFooter />

    <!-- Global Quote Modal -->
    <QuoteModal :is-open="isQuoteModalOpen" @close="closeQuoteModal" />
  </div>
</template>

<style scoped>
.app-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
}
</style>
