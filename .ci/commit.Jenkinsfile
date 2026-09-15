node {
    def app

    
    stage('Clone repository') {
      
      
        checkout scm
    }
    
    stage('Update GIT') {
            script {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withCredentials([
		                usernamePassword(
		                    credentialsId: 'maingithub',
		                    passwordVariable: 'GIT_PASSWORD',
		                    usernameVariable: 'GIT_USERNAME'
		                ),
		                string(
		                    credentialsId: 'dockerlogin-name',
		                    variable: 'DOCKER_NAME'
		                ),
		                string(
		                    credentialsId: 'git-email',
		                    variable: 'GIT_EMAIL'
		                ),
		                string(
		                    credentialsId: 'git-name',
		                    variable: 'GIT_NAME'
		                )
                        ]) {
                            sh 'git config --replace-all user.email ${GIT_EMAIL}'
                            sh 'git config --replace-all user.name "${GIT_NAME}"'
                            sh 'cat ${APP_NAME}.yaml'
                            sh 'sed -i "s+${DOCKER_NAME}/${APP_NAME}.*+${DOCKER_NAME}/${APP_NAME}:${DOCKERTAG}+g" ${APP_NAME}.yaml'
                            sh 'cat ${APP_NAME}.yaml'
                            sh 'git add .'
                            sh 'git commit -m "Done by Jenkins Job deployment: ${BUILD_NUMBER}"'
                            sh 'git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/${APP_NAME}.git HEAD:main'
                    }
                }
            }
    }

}

