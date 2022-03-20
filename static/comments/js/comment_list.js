const form_comments = document.querySelectorAll(
  ".form-comment-list-input-container-global"
);
const comment_options_btn = document.querySelectorAll(".comment-options-btn");

form_comments.forEach((form) => {
  form.addEventListener("submit", (e) => {
    const input_text_comment = document.getElementById(
      "input_message_comment-" + e.target.title
    ).value;
    const input_hidden_post_comment = document.getElementById(
      "input_hidden_post_comment-" + e.target.title
    ).value;
    const input_hidden_post_comment2 = document.getElementById(
      "input_hidden_post_comment2-" + e.target.title
    ).value;
    // alert(`${input_text_comment} - ${input_hidden_post_comment}`)
    const container_list_comment = document.getElementById(
      "container-global-comment-list-" + e.target.title
    );
    e.preventDefault();

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

    fetch("/post/", {
      method: "POST",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({
        message: input_text_comment,
        id_post: input_hidden_post_comment,
        id_comment: input_hidden_post_comment2,
      }),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        console.log(data);
        console.log(data.comment_message);

        const verif_img = (v) => {
          if (v) {
            return `<img id="container-comment-list-img-profile" src="http://127.0.0.1:8000${v}" />`;
          } else {
            return `<img id="container-comment-list-img-profile" src="http://127.0.0.1:8000/static/components/img/user.svg" />`;
          }
        };

        const verif_author = (author_comment, author_post) => {
          if (author_comment === author_post) {
            return `<span id="author_post_and_comment">Auteur</span>`;
          } else {
            return "";
          }
        };
        //

        if (!input_hidden_post_comment2) {
          container_list_comment.innerHTML += `
            <div class="container-comment-list">

            <div id="${data.id}" class="comment-options-btn">
              <span id="btn-point"></span>
              <span id="btn-point"></span>
              <span id="btn-point"></span>
            </div>
          
            <div id="comment-options-container${
              data.id
            }" class="comment-options-actions-container display-none">
              <ul>
                <div href="#" class="comment-options-item comment-options-item-edit" title="${
                  data.id
                }">
                  <img src="http://127.0.0.1:8000/static/comments/img/edit.svg" id="${
                    data.id
                  }" class="comment-options-item-img">
                  <span class="btn-edit-comment comment-options-item-span" id="${
                    data.id
                  }">Modifier</span>
                </div>
                <a href="#" class="comment-options-item comment-options-item-delete">
                  <img src="http://127.0.0.1:8000/static/comments/img/delete.svg" id="${
                    data.id
                  }" class="comment-options-item-img">
                  <span class="btn-del-comment comment-options-item-span" id="${
                    data.id
                  }">Supprimer</span>
                </a>
              </ul>
            </div>

              ${verif_img(
                data.user_profile_img
              )}              <div class="comment-content-box">
                <div class="comment-info-content">
                  <div class="comment-info-content-I" id="comment-info-content-I-${
                    data.post_id
                  }">
                    <strong>${data.comment_author_first_name}
                      ${data.comment_author_last_name}
                      ${verif_author(data.comment_author, data.post_author)}
                    </strong>
                    <small>${data.comment_date_added}</small>
                  </div>
                  <p id="comment-author-profile-title">${
                    data.user_profile_bio
                  }</p>
                </div>
                <div class="comment-text-content">
                  <p class="msg-text-p-${data.id}" id="${data.post_id}">${
            data.comment_message
          }</p>
                </div>
              </div>
            </div>`;
        } else {
          document.querySelector(".msg-text-p-" + data.id).textContent =
            data.comment_message;
        }
      });
    document.getElementById("input_message_comment-" + e.target.title).value =
      "";
  });
});

comment_options_btn.forEach((element) => {
  element.addEventListener("click", (e) => {
    comment_ops_container = document.getElementById(
      "comment-options-container" + element.id
    );
    comment_ops_container.classList.toggle("display-none");
  });
});

// ***

const comment_options_item_edits = document.querySelectorAll(
  ".comment-options-item-edit"
);

comment_options_item_edits.forEach((element) => {
  element.addEventListener("click", (e) => {
    const msg = document.querySelector(".msg-text-p-" + e.target.id);
    console.log(e.target.id);
    console.log(msg.id);

    document.getElementById("input_message_comment-" + msg.id).value =
      msg.textContent;
    document.getElementById("input_hidden_post_comment2-" + msg.id).value =
      e.target.id;
  });
});

// const form_comments = document.querySelectorAll(".form-comment");
// const csrf = document.getElementsByName("csrfmiddlewaretoken");

// document.addEventListener("DOMContentLoaded", () => {
//   form_comments.forEach((form_comment) => {
//     form_comment.addEventListener("submit", (e) => {
//       e.preventDefault();
//       const aside_comment = document.getElementById(
//         "aside-comment-" + e.target.title
//       );
//       const csrf = document.getElementsByName("csrfmiddlewaretoken");
//       const input_text_comment = document.getElementById(
//         "input_message_comment-" + e.target.title
//       );
//       const input_hidden_post_comment = document.getElementById(
//         "input_hidden_post_comment-" + e.target.title
//       );
//       // const comment_count_by_post = document.getElementById(
//       //   "comments-num" + e.target.title
//       // );

//       const fd = new FormData();
//       fd.append("csrfmiddlewaretoken", csrf[0].value);
//       fd.append("message", input_text_comment.value);
//       fd.append("post_id", input_hidden_post_comment.value);

//       $.ajax({
//         type: "POST",
//         url: `/comment/${e.target.title}/add-comment/`,
//         data: fd,
//         success: function (response) {
//           const data = JSON.parse(JSON.stringify(response.data[0]));
//           //   console.log(data);
//           //   console.log(data.comment_author);
//           // input_text_comment.value = "";

//           // const count_num_comment = parseInt(comment_count_by_post.textContent);
//           // console.log(count_num_comment + 100);

//           const verif_img = (v) => {
//             if (v) {
//               return `<img id="container-comment-list-img-profile" src="http://127.0.0.1:8000${v}" />`;
//             } else {
//               return `<img id="container-comment-list-img-profile" src="http://127.0.0.1:8000/static/components/img/user.svg" />`;
//             }
//           };

//           const verif_author = (author_comment, author_post) => {
//             if (author_comment === author_post) {
//               return `<span id="author_post_and_comment">Auteur</span>`;
//             }
//           };

//           aside_comment.innerHTML += `<div class="container-comment-list">
//           ${verif_img(data.user_profile_img)}
//                 <div class="comment-content-box">
//                 <div class="comment-info-content">
//                     <div class="comment-info-content-I">
//                     <strong>${data.comment_author_first_name}
//                     ${data.comment_author_last_name}
//                     ${verif_author(data.comment_author, data.post_author)}

//                     </strong>
//                     <small>${data.comment_date_added}</small>
//                     </div>
//                     <p id="comment-author-profile-title">${
//                       data.user_profile_bio
//                     }</p>
//                 </div>
//                 <div class="comment-text-content">
//                     <p>${data.comment_message}</p>
//                 </div>
//                 </div>
//             </div>`;
//         },
//         error: function (error) {
//           console.log(error);
//         },
//         cache: false,
//         contentType: false,
//         processData: false,
//       });
//     });
//   });
// });

// $(document).ready(function () {
//   $(".form-comment").submit(function (e) {
//     e.preventDefault();

//     const post_id = $(this).attr("title");
//     const url = $(this).attr("action");

//     const aside_comment = $(`#aside-comment-${post_id}`);
//     const input_text_comment = $(`#input_message_comment-${post_id}`);
//     const input_hidden_post_comment = $(
//       `#input_hidden_post_comment-${post_id}`
//     );

//     // const csrf = document.querySelector(`input[name=csrfmiddlewaretoken]`);
//     // console.log(csrf.value);
//     // console.log(input_hidden_post_comment.val());

//     $.ajax({
//       type: "POST",
//       url: url,
//       data: {
//         csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
//         id: input_hidden_post_comment.val(),
//         message: input_text_comment.val(),
//       },
//       success: function (response) {
//         const data = JSON.parse(JSON.stringify(response.data[0]));
//         console.log(data);
//         console.log(data.comment_author);
//         input_text_comment.val("");

//         function verif_img(v) {
//           if (v) {
//             return `<img id="container-comment-list-img-profile" src="http://127.0.0.1:8000${v}" />`;
//           } else {
//             return `<img id="container-comment-list-img-profile" src="http://127.0.0.1:8000/static/components/img/user.svg" />`;
//           }
//         }

//         function verif_author(author_comment, author_post) {
//           if (author_comment === author_post) {
//             return `<span id="author_post_and_comment">Auteur</span>`;
//           }
//         }

//         content_comment = `<div class="container-comment-list">
//             ${verif_img(data.user_profile_img)}
//                   <div class="comment-content-box">
//                   <div class="comment-info-content">
//                       <div class="comment-info-content-I">
//                       <strong>${data.comment_author_first_name}
//                       ${data.comment_author_last_name}
//                       ${verif_author(data.comment_author, data.post_author)}

//                       </strong>
//                       <small>${data.comment_date_added}</small>
//                       </div>
//                       <p id="comment-author-profile-title">${
//                         data.user_profile_bio
//                       }</p>
//                   </div>
//                   <div class="comment-text-content">
//                       <p>${data.comment_message}</p>
//                   </div>
//                   </div>
//               </div>
//           `;

//         aside_comment.append(content_comment);
//       },
//       error: function (error) {
//         console.log(error);
//       },
//       cache: false,
//       contentType: false,
//       processData: false,
//     });
//   });
// });
