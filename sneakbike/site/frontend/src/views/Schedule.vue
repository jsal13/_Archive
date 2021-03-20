<template>
  <div class="schedule">
    <v-row justify="center">
      <v-col cols="12">
        <h1>Sneakbike Schedule</h1>
        <p>
          To add the Sneakbike calendar to your Google Calendar, click the
          <b>"+GoogleCalendar"</b> button in the lower-right corner.
        </p>
        <div class="responsive-iframe-container big-container">
          <iframe
            src="https://calendar.google.com/calendar/embed?height=400&amp;wkst=1&amp;bgcolor=%233f51b5&amp;ctz=America%2FChicago&amp;src=c25lYWtiaWtlQGdtYWlsLmNvbQ&amp;color=%23039BE5&amp;showNav=1&amp;showDate=1&amp;showPrint=0&amp;showCalendars=1&amp;mode=WEEK"
            style="border-width:0"
            width="100%"
            height="600"
            frameborder="0"
            scrolling="no"
          ></iframe>
        </div>
        <div class="responsive-iframe-container small-container">
          <iframe
            src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=America%2FChicago&amp;src=c25lYWtiaWtlQGdtYWlsLmNvbQ&amp;color=%23039BE5&amp;mode=AGENDA&amp;showPrint=0&amp;showCalendars=0&amp;showTitle=1"
            style="border:solid 1px #777"
            width="800"
            height="600"
            frameborder="0"
            scrolling="no"
          ></iframe>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Schedule",
};
</script>

<style>
@media (max-width: 550px) {
  .big-container {
    display: none;
  }
}
@media (min-width: 550px) {
  .small-container {
    display: none;
  }
}
/* Responsive iFrame */
.responsive-iframe-container {
  position: relative;
  padding-bottom: 56.25%;
  padding-top: 30px;
  height: 0;
  overflow: hidden;
}
.responsive-iframe-container iframe,
.vresponsive-iframe-container object,
.vresponsive-iframe-container embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
