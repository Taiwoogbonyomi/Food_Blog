document.addEventListener('DOMContentLoaded', function() {
    // Handle comment form submission
    var commentForms = document.querySelectorAll('form.comment-form');
    commentForms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            var formData = new FormData(form);
            var url = form.action;

            fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                // Handle success
                if (data.success) {
                    addCommentToDOM(data.comment);
                    form.reset();
                } else {
                    alert('Failed to add comment: ' + data.message);
                }
            })
            .catch(function(error) {
                console.error('Error:', error);
            });
        });
    });

    // Handle upvote and downvote buttons
    var upvoteButtons = document.querySelectorAll('.btn-upvote');
    var downvoteButtons = document.querySelectorAll('.btn-downvote');

    upvoteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            handleVote(button, 'upvote');
        });
    });

    downvoteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            handleVote(button, 'downvote');
        });
    });

    function handleVote(button, voteType) {
        var recipeId = button.dataset.recipeId;
        var url = button.closest('form').action;

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ voteType: voteType, recipeId: recipeId }),
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            if (data.success) {
                // Update vote count in the DOM
                var voteCount = button.querySelector('.vote-count');
                if (voteType === 'upvote') {
                    voteCount.textContent = data.newUpvoteCount;
                } else {
                    voteCount.textContent = data.newDownvoteCount;
                }
            } else {
                alert('Failed to cast vote: ' + data.message);
            }
        })
        .catch(function(error) {
            console.error('Error:', error);
        });
    }

    // Helper function to add a new comment to the DOM
    function addCommentToDOM(comment) {
        var commentList = document.querySelector('.comment-list');
        var commentItem = document.createElement('li');
        commentItem.classList.add('media', 'my-4');
        commentItem.innerHTML = '<div class="media-body"><h5 class="mt-0 mb-1">' + comment.author + '</h5><p>' + comment.content + '</p><small class="text-muted">' + new Date(comment.created_at).toLocaleString() + '</small></div>';
        commentList.appendChild(commentItem);
    }

    // Function to get CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
