$(document).ready(function() {
    $('.select-keahlian').selectmenu();
    $('.select-level').selectmenu();
});

const addKeahlian = function() {
    keahlian = $('.skill-baru').val();
    level = $('.level-baru').val();
    console.log(keahlian);
    console.log(level);
    location.href = 'add-keahlian/'+ keahlian + '/' + level + '/';
}

$(".delete-button").on("click", function(e) {
    var uid = $(this).data('id');
    location.href="delete-keahlian/" + uid;
});

// Setup an event listener to make an API call once auth is complete
function onLinkedInLoad() {
    IN.Event.on(IN, "auth", getProfileData);

}

// Use the API call wrapper to request the member's profile data
function getProfileData() {
    IN.API.Profile("me").fields("id", "first-name", "last-name", "headline", "location", "picture-url", "public-profile-url", "email-address").result(displayProfileData).error(onError);
}

// Handle the successful return from the API call
function displayProfileData(data){
    var user = data.values[0];
    $(".temp-foto img").attr("src",user.pictureUrl);
    $(".nama").html("    " + user.firstName+' '+user.lastName);
    $(".email").html("    " + user.emailAddress);
    $(".profile-linkedin").html("    " + user.publicProfileUrl);
    $(".data").css({
        "margin-bottom": "3px", 
    });
    $(".some-words").css({
        "transform" : "translatey(20px)", 
    });
}

// Handle an error response from the API call
function onError(error) {
    console.log(error);
}

// Destroy the session of linkedin
function logout(){
    IN.User.logout();
}

var hubungkanLinkedin = function(boolean_rahasia, nama, email, linkedin_link, foto_profil) {
    $.ajax({
        method: "POST",
        url: '/mahasiswa/edit-profile/save/',
        data: { 
            boolean_rahasia : boolean_rahasia, 
            nama: nama, 
            email: email, 
            linkedin_link : linkedin_link, 
            foto_profil : foto_profil, 
            csrfmiddlewaretoken : '{{ csrf_token }}'},
        success : function () {
            window.location.replace('/mahasiswa/profile/')
        },
        error : function (error) {
            alert("Gagal menghubungkan")
        }
    });
};

function save_data_linkedin() {
    IN.User.authorize(auth => {
        console.log(auth);
        IN.API.Profile("me").fields("id", "first-name", "last-name", "headline", "location", "picture-url", "public-profile-url", "email-address")
        .result(data => {
            console.log(data);
            var boolean_rahasia = document.getElementsByName('bool');
            for (var i = 0, length = boolean_rahasia.length; i < length; i++)
            {
                if (boolean_rahasia[i].checked)
                {
                boolean_rahasia = boolean_rahasia[i].value;
                }
            }
            const user = data.values[0];
            const nama = user.firstName + ' ' + user.lastName;
            const email = user.emailAddress;
            const linkedin_link = user.publicProfileUrl;
            const foto_profil = user.pictureUrl;
            hubungkanLinkedin(boolean_rahasia, nama, email, linkedin_link, foto_profil);
            }
        )}
    )}

    $('.save-button').on("click", function(e) {
        save_data_linkedin();
    });

    $('.exit-button').on("click", function(e) {
        location.href = '/mahasiswa/profile/'
    });


