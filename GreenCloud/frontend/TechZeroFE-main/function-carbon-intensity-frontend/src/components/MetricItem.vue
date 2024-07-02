<template>
  <div class="item">
    <div class="details">
      <h3>
        <slot name="heading"></slot>
      </h3>
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.item {
  background-color: white;
  border-radius: 10px;
  padding: 10px;
}

.details {
  flex: 1;
  margin-left: 1rem;
}

h3 {
  font-size: 1.1rem;
  font-weight: 500;
}
</style>
