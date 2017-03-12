'use strict';

angular.module('loginDetail').
    component('loginDetail', {
        templateUrl: '/api/templates/login-detail.html',
        controller: function(
            $cookies,
            $http,
            $location,
            $routeParams,
            $rootScope,
            $scope
        ){
            var loginUrl = '/api/auth/token/'
            $scope.user = {
            }

            var tokenExists = $cookies.get("token")
            if (tokenExists) {
                // verify token
                $scope.loggedIn = true;
                $cookies.remove("token")
                $scope.user = {
                    username: $cookies.get("username")
                }
            }

            $scope.doLogin = function(user){
                console.log(user)

                var reqConfig = {
                    method: "POST",
                    url: loginUrl,
                    data: {
                        username: user.username,
                        password: user.password
                    },
                    headers: {}
                }
                var requestAction = $http(reqConfig)

                requestAction.then(function(response){
                        // console.log(r_data) // token
                        $cookies.put("token", response.data.token)
                        $cookies.put("username", user.username)
                        // message
                        $location.path("/")
                })
            }
            // $http.post()
        }
})
