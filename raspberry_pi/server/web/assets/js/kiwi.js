$(window).on("resize", renderPage);
$(document).ready(renderPage);


$(".prev").click(function() {
  $("#content").dragend("right");
});

$(".next").click(function() {
  $("#content").dragend("left");
});

$(".nav").click(function(event) {
  var page = $(event.target).data("page");
  $("#content").dragend({
    scrollToPage: page
  });
  $(event.target).addClass("active");
});

function renderPage(event) {
  $(".nav").fadeIn('slow')

  $("#content").dragend({
    onSwipeEnd: function() {
      var first = this.pages[0],
          last = this.pages[this.pages.length - 1];

      $(".prev, .next").removeClass("deactivated");
      $(".nav li").removeClass("active");

      if (first === this.activeElement) {
        $(".prev").addClass("deactivated")
      };

      if (last === this.activeElement) {
        $(".next").addClass("deactivated")
      }
      $(".nav li").eq(this.page).addClass("active");

      var movementJoystick = nipplejs.create({
    		zone: document.getElementById('movement_joystick_zone'),
    		color: 'red',
        mode: 'dynamic'
    	});

    }
  }).fadeIn('slow');
}
