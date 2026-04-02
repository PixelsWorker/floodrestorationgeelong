<script setup>
import SiteHeader from './components/SiteHeader.vue'
import HeroSection from './components/HeroSection.vue'
import TrustBar from './components/TrustBar.vue'
import ServicesSection from './components/ServicesSection.vue'
import HowItWorks from './components/HowItWorks.vue'
import WhyChooseUs from './components/WhyChooseUs.vue'
import EmergencyBanner from './components/EmergencyBanner.vue'
import TestimonialsSection from './components/TestimonialsSection.vue'
import ServiceAreas from './components/ServiceAreas.vue'
import FaqSection from './components/FaqSection.vue'
import ContactSection from './components/ContactSection.vue'
import SiteFooter from './components/SiteFooter.vue'
</script>

<template>
  <div class="app-wrapper">
    <SiteHeader />
    <main>
      <HeroSection />
      <TrustBar />
      <ServicesSection />
      <HowItWorks />
      <WhyChooseUs />
      <EmergencyBanner />
      <TestimonialsSection />
      <ServiceAreas />
      <FaqSection />
      <ContactSection />
    </main>
    <SiteFooter />
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
