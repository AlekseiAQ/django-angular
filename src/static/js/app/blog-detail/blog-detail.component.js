'use strict';

angular.module('blogDetail').
    component('blogDetail', {
        templateUrl: '/api/templates/blog-detail.html',
        controller: function(Post, $cookies, $http, $location, $routeParams, $scope){
            var slug = $routeParams.slug
            Post.get({"slug": slug}, function(data) {
                $scope.post = data
                $scope.comments = data.comments
            })
            // Post.query(function(data){
            //     $scope.notFound = true
            //     $scope.comments = []
            //     angular.forEach(data, function(post){
            //         if (post.id == $routeParams.id){
            //             $scope.notFound = false
            //             $scope.post = post
            //             if (post.comments) {
            //                 $scope.comments = post.comments
            //             }
            //             resetReply()
            //         }
            //     })
            // })


            $scope.deleteComment = function(comment) {
                $scope.$apply(
                    $scope.comments.splice(comment, 1)
                )
                // someResource.$delete()
            }


            $scope.addReply = function() {
                console.log($scope.reply)
                var token = $cookies.get("token")
                if (token) {
                    var req = {
                        method: "POST",
                        url: '' + slug + '',
                        data: {
                            content: $scope.reply.content
                        },
                        headers: {
                            authorization: "JWT " + token
                        }
                    }
                    var requestAction = $http(req)
                    requestAction.then(function(response) {
                        $scope.comments.push($scope.reply)
                        resetReply()
                    }, function(e_response) {
                        console.log("Error. Statuts code: " + e_response.status)
                    })
                    // $scope.comments.push("abc")
                } else {
                    console.log("no token")
                }
            }

            function resetReply(){
                $scope.reply = {
                    id: $scope.comments.length + 1,
                    content: "",
                }
            }

            if ($scope.notFound) {
                console.log("Not found")
                // change location
                $location.path("/")
            }

    }
});
