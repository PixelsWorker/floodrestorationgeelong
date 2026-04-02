<script setup>
import { ref } from 'vue'

const activeTab = ref(0)

const tabs = [
  {
    title: 'Inspection & Assessment',
    heading: '1. Detailed Inspection and Damage Assessment',
    content: 'Every successful restoration begins with a comprehensive inspection. Our technicians assess the full extent of the flood or water damage, identify hidden moisture, and create a customised restoration plan tailored to your property.',
    note: 'Pro tip: take photos before we arrive — it helps with documentation and insurance claims.'
  },
  {
    title: 'Water Removal',
    heading: '2. Fast and Efficient Water Removal',
    content: 'The next critical stage is water extraction. Using high-powered truck-mounted equipment, we remove standing water quickly and efficiently. This rapid response reduces further damage to floors, walls, and furniture.',
    note: null
  },
  {
    title: 'Drying & Dehumidification',
    heading: '3. Advanced Drying and Dehumidification',
    content: 'Once the visible water is gone, we move on to thorough drying and dehumidification. Even when surfaces appear dry, moisture often lingers deep within walls, floors, and ceilings. Our advanced drying equipment eliminates hidden dampness.',
    note: null
  },
  {
    title: 'Sanitising & Mould Prevention',
    heading: '4. Cleaning, Sanitising & Mould Prevention',
    content: 'After drying, we clean and sanitise every affected surface, restoring hygiene and freshness to your property. Our team disinfects walls, flooring, and furniture using eco-friendly antimicrobial cleaning solutions.',
    note: null
  },
  {
    title: 'Final Restoration',
    heading: '5. Final Restoration & Quality Check',
    content: 'In the final stage, we complete a thorough property restoration, ensuring everything is safe, clean, and restored to pre-damage condition. We apply anti-microbial sprays and perform final inspections.',
    note: null
  }
]
</script>

<template>
  <section class="how-it-works">
    <div class="container">
      <div class="section-title">
        <h2>Our Process: A Step-by-Step Guide to Recovery</h2>
        <p>Knowing what to expect can greatly lessen stress during a crisis.</p>
      </div>

      <div class="tabs-container">
        <div class="tabs-nav">
          <button 
            v-for="(tab, index) in tabs" 
            :key="index"
            class="tab-btn"
            :class="{ active: activeTab === index }"
            @click="activeTab = index"
          >
            <span class="num">{{ index + 1 }}</span>
            <span class="title">{{ tab.title }}</span>
          </button>
        </div>

        <div class="tabs-content">
          <transition name="fade" mode="out-in">
            <div :key="activeTab" class="tab-panel">
              <h4>{{ tabs[activeTab].heading }}</h4>
              <p>{{ tabs[activeTab].content }}</p>
              <div v-if="tabs[activeTab].note" class="note">
                <strong>Pro Tip:</strong> {{ tabs[activeTab].note }}
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.how-it-works {
  background-color: var(--bg-light);
}

.section-title {
  text-align: center;
  margin-bottom: 50px;
}

.tabs-container {
  display: flex;
  background: var(--white);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-main);
  min-height: 400px;
}

.tabs-nav {
  flex: 0 0 320px;
  background: linear-gradient(180deg, #f7fbff, #eef6ff);
  padding: 20px;
  border-right: 1px solid rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 15px;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  text-align: left;
  transition: var(--transition-fast);
  width: 100%;
}

.tab-btn:hover {
  background-color: rgba(0, 119, 204, 0.05);
  transform: translateX(5px);
}

.tab-btn.active {
  background: linear-gradient(90deg, var(--primary-color), var(--primary-hover));
  color: var(--white);
  box-shadow: 0 5px 15px rgba(0, 119, 204, 0.2);
}

.num {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-accent);
  color: var(--primary-color);
  border-radius: 50%;
  font-weight: 700;
  font-size: 14px;
}

.active .num {
  background: var(--white);
  color: var(--primary-color);
}

.tab-btn .title {
  font-weight: 600;
  font-size: 15px;
}

.tabs-content {
  flex: 1;
  padding: 40px;
}

.tab-panel h4 {
  font-size: 24px;
  color: var(--secondary-color);
  margin-bottom: 20px;
}

.tab-panel p {
  color: var(--text-light);
  line-height: 1.8;
  font-size: 16px;
}

.note {
  margin-top: 25px;
  padding: 15px;
  background-color: var(--bg-accent);
  border-left: 4px solid var(--primary-color);
  border-radius: 4px;
  font-style: italic;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@media (max-width: 900px) {
  .tabs-container {
    flex-direction: column;
  }
  
  .tabs-nav {
    flex: none;
    border-right: none;
    border-bottom: 1px solid rgba(0,0,0,0.05);
    flex-direction: row;
    overflow-x: auto;
    padding: 15px;
  }
  
  .tab-btn {
    flex: 0 0 auto;
    width: auto;
    padding: 10px 15px;
  }
  
  .tab-btn span.title {
    display: none;
  }

  .tab-btn.active span.title {
    display: inline;
  }
}
</style>
