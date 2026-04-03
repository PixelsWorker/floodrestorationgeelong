<template>
  <div class="site-header" @click.stop>
    <div class="top-bar" @click.stop>
      <!-- Top bar content -->
    </div>
    <header @click.stop>
      <!-- Header content -->
      <button @click.stop="toggleMenu">Hamburger</button>
      <submenu v-show="isVisible">
        <!-- Submenu content -->
      </submenu>
    </header>
  </div>
</template>

<script setup>
// Removed stray brace and other script content

</script>