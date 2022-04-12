// $(document).ready(function () {
//   $(".like-form").submit(function (e) {
//     // stoper le rechargement de la page lorsque on clique btn like
//     e.preventDefault();

//     // selectionner l'id du formulaire
//     const post_id = $(this).attr("id");

//     // selectionner le text de btn like (j'aime ou je n'aime pas)
//     const likeText = $(`.like-text${post_id}`).text();

//     // selectionner l'url de l'action du formulaire
//     const url = $(this).attr("action");

//     // declarer une variable res pour compter le nombre de like
//     let res;

//     // selectionner le text de nombre de like et convertir en string
//     const likes_count = $(`#likes-num${post_id}`);
//     const likes_num = parseInt(likes_count.text());

//     // selectionner le text de nombre de like et convertir en string
//     const likes_text_plural = $(`#text-plural${post_id}`);
//     // console.log(img_like);
//     // console.log($(`#text-plural${post_id}`).text());

//     const fonc_text_plural = (n) => {
//       if (n > 1) {
//         likes_text_plural.text("Likes");
//       } else {
//         likes_text_plural.text("Like");
//       }
//     };

//     // ajax avec method POST sans rechargement de la page
//     $.ajax({
//       type: "POST",
//       url: url,
//       data: {
//         csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
//         post_id: post_id,
//       },

//       success: function (response) {
//         `condition
//        si le text de btn like est 'Je n'aime pas':
//         - change le text en 'J'aime'
//         - change le icone like.svg en unlike.svg
//         - affecter la variable res à likes_count + 1
//         - mettre à jour le nombre de like avec la variable res
//         sinon :
//         - change le text en 'Je n'aime pas'
//         - change le icone like.svg en like.svg
//         - affecter la variable res à likes_count - 1
//         - mettre à jour le nombre de like avec la variable res`;

//         if (response.value === "Unlike") {
//           //                         $(`.like-text${post_id}`).text("J'aime");
//           // $(`.like-text${post_id}`).css("color","#f1f1f1")
//           $(`.like-text${post_id}`).removeClass("text-like_unlike-span");
//           $(`#like-img${post_id}`).prop(
//             "src",
//             "http://127.0.0.1:8000/static/post/img/unlike.svg"
//             // '{% static "post/img/unlike.svg" %}'
//           );
//           res = likes_num - 1;
//           fonc_text_plural(res);
//         } else {
//           //                         $(`.like-text${post_id}`).text("Je n'aime pas");
//           // $(`.like-text${post_id}`).css("color","#1abc9c")
//           $(`.like-text${post_id}`).addClass("text-like_unlike-span");
//           $(`#like-img${post_id}`).prop(
//             "src",
//             "http://127.0.0.1:8000/static/post/img/like.svg"
//             // '{% static "post/img/like.svg" %}'
//           );
//           res = likes_num + 1;
//           fonc_text_plural(res);
//         }

//         likes_count.text(res);
//       },
//       error: function (response) {
//         // console.log('error', response);
//       },
//     });
//   });
// });

const form_like_post = document.querySelectorAll(".like-form")



form_like_post.forEach((form) => {
  form.addEventListener("submit", function (e) {
    // stoper le rechargement de la page lorsque on clique btn like
    e.preventDefault();

    console.log(e.target.action);

    // selectionner l'id du formulaire
    const post_id = e.target.id;
    // console.log(post_id);

    // selectionner le text de btn like (j'aime ou je n'aime pas)
    const likeText = document.querySelector(`.like-text${post_id}`).textContent;
    // console.log(likeText);

    // selectionner l'url de l'action du formulaire
    const url = e.target.action;

    // declarer une variable res pour compter le nombre de like
    let res;

    // selectionner le text de nombre de like et convertir en string
    const likes_count = document.getElementById(`likes-num${post_id}`);
    // console.log(likes_count);
    const likes_num = parseInt(likes_count.textContent);
    // console.log(likes_num);

    // selectionner le text de nombre de like et convertir en string
    const likes_text_plural = document.getElementById(`text-plural${post_id}`);
    // console.log(img_like);
    // console.log($(`#text-plural${post_id}`).text());

    const fonc_text_plural = (n) => {
      if (n > 1) {
        likes_text_plural.textContent = "Likes";
      } else {
        likes_text_plural.textContent = "Like";
      }
    };


    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    const csrftoken = getCookie("csrftoken");

    const formData = new FormData();
      formData.append("post_id", post_id);

      const request = new Request(url, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrftoken,
        },
        body: formData,
      });

      fetch(request)
        .then((response) => response.json())
        .then((response) => {
          `condition
       si le text de btn like est 'Je n'aime pas':
        - change le text en 'J'aime'
        - change le icone like.svg en unlike.svg
        - affecter la variable res à likes_count + 1
        - mettre à jour le nombre de like avec la variable res
        sinon :
        - change le text en 'Je n'aime pas'
        - change le icone like.svg en like.svg
        - affecter la variable res à likes_count - 1
        - mettre à jour le nombre de like avec la variable res`;

        if (response.value === "Unlike") {
          document.querySelector(`.like-text${post_id}`).classList.remove("text-like_unlike-span");
          document.getElementById(`like-img${post_id}`).src = "/static/post/img/unlike.svg"
           
          res = likes_num - 1;
          fonc_text_plural(res);
        } else {
          document.querySelector(`.like-text${post_id}`).classList.add("text-like_unlike-span");
          document.getElementById(`like-img${post_id}`).src = "/static/post/img/like.svg"
         
          res = likes_num + 1;
          fonc_text_plural(res);
        }

        likes_count.textContent = res;
        });
  });
});
