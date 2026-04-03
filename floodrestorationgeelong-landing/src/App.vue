<script setup>
import { ref, provide, defineAsyncComponent } from 'vue'
import SiteHeader from './components/SiteHeader.vue'
import HeroSection from './components/HeroSection.vue'

// Below-fold components - Lazy Loaded
const ServicesSection = defineAsyncComponent(() => import('./components/ServicesSection.vue'))
const TrustBar = defineAsyncComponent(() => import('./components/TrustBar.vue'))
const HowItWorks = defineAsyncComponent(() => import('./components/HowItWorks.vue'))
const VideoSection = defineAsyncComponent(() => import('./components/VideoSection.vue'))
const EmergencyBanner = defineAsyncComponent(() => import('./components/EmergencyBanner.vue'))
const TestimonialsSection = defineAsyncComponent(() => import('./components/TestimonialsSection.vue'))
const FaqSection = defineAsyncComponent(() => import('./components/FaqSection.vue'))
const ContactSection = defineAsyncComponent(() => import('./components/ContactSection.vue'))
const SiteFooter = defineAsyncComponent(() => import('./components/SiteFooter.vue'))
const QuoteModal = defineAsyncComponent(() => import('./components/QuoteModal.vue'))

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
