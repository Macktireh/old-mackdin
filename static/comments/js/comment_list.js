const form_comments = document.querySelectorAll(".form-comment");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
// const form_comments = document.querySelectorAll(".btn-send-comment");

// document.addEventListener("DOMContentLoaded", () => {
//   form_comments.forEach((form_comment) => {
//     form_comment.addEventListener("submit", (e) => {
//       e.preventDefault();
//       console.log("ok");
//     });
//   });
// });

document.addEventListener("DOMContentLoaded", () => {
  form_comments.forEach((form_comment) => {
    form_comment.addEventListener("submit", (e) => {
      e.preventDefault();
      const aside_comment = document.getElementById(
        "aside-comment-" + e.target.title
      );
      const csrf = document.getElementsByName("csrfmiddlewaretoken");
      const input_text_comment = document.getElementById(
        "input_message_comment-" + e.target.title
      );
      const input_hidden_post_comment = document.getElementById(
        "input_hidden_post_comment-" + e.target.title
      );
      // const comment_count_by_post = document.getElementById(
      //   "comments-num" + e.target.title
      // );

      const fd = new FormData();
      fd.append("csrfmiddlewaretoken", csrf[0].value);
      fd.append("message", input_text_comment.value);
      fd.append("post_id", input_hidden_post_comment.value);

      $.ajax({
        type: "POST",
        url: `/comment/${e.target.title}/add-comment/`,
        data: fd,
        success: function (response) {
          const data = JSON.parse(JSON.stringify(response.data[0]));
          //   console.log(data);
          //   console.log(data.comment_author);
          // input_text_comment.value = "";

          // const count_num_comment = parseInt(comment_count_by_post.textContent);
          // console.log(count_num_comment + 100);

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
            }
          };

          aside_comment.innerHTML += `<div class="container-comment-list">
          ${verif_img(data.user_profile_img)}
                <div class="comment-content-box">
                <div class="comment-info-content">
                    <div class="comment-info-content-I">
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
                    <p>${data.comment_message}</p>
                </div>
                </div>
            </div>`;
        },
        error: function (error) {
          console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
      });
    });
  });
});

// const comment_options_btn = document.querySelectorAll(".comment-options-btn");

// comment_options_btn.forEach((element) => {
//   element.addEventListener("click", (e) => {
//     comment_ops_container = document.getElementById(
//       "comment-options-container" + element.id
//     );
//     comment_ops_container.classList.toggle("display-none");
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
