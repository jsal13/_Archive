<template>
  <div class="warning-card custom-tiny-card">
    <v-row>
      <v-col class="ma-4 pa-4">
        <v-card class="mx-auto warning" outlined>
          <v-card-text>
            <div class="text-button">Warning</div>
            <p class="text-body-2">
              <slot></slot>
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "WarningCard",
};
</script>