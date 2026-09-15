pipeline {
	agent {
	    kubernetes {
                podRetention onFailure()
                yaml '''
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: agent
spec:
  volumes:
  - name: ca
    configMap:
      name: jenkins-ca
  - name: truststore
    emptyDir: {}
  - name: kaniko
    secret:
      secretName: kaniko-docker
  initContainers:
  - name: importer
    image: eclipse-temurin:17-alpine
    command:
      - sh
      - -c
      - |
        cp $JAVA_HOME/lib/security/cacerts /custom-truststore/cacerts
        keytool -importcert -noprompt -alias jenkins \
        -file /ca-cert/root-ca.crt \
        -keystore /custom-truststore/cacerts \
        -storepass changeit
    volumeMounts:
    - name: ca
      mountPath: /ca-cert
    - name: truststore
      mountPath: /custom-truststore
  containers:
  - name: jnlp
    env:
      - name: JENKINS_JAVA_OPTS
        value: "-Djavax.net.ssl.trustStore=/custom-truststore/cacerts -Djavax.net.ssl.trustStorePassword=changeit"
    volumeMounts:
    - name: truststore
      mountPath: /custom-truststore
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command: ['cat']
    tty: true
    volumeMounts:
    - name: kaniko
      mountPath: /kaniko/.docker/config.json
      subPath: .dockerconfigjson
'''
	    }
	}
 	stages {
		stage('Package') {
		    steps {
		      echo 'Packaging ${APP_NAME} with docker'
		      container('kaniko') {
		          withCredentials([usernamePassword(credentialsId: 'dockerlogin', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
		              sh '''
		                  /kaniko/executor \
		                  --context=dir://${WORKSPACE} \
		                  --dockerfile=${WORKSPACE}/Dockerfile \
		                  --destination=${DOCKER_USERNAME}/${APP_NAME}:${GIT_COMMIT}
		              '''
		              sh '''
		                  /kaniko/executor \
		                  --context=dir://${WORKSPACE} \
		                  --dockerfile=${WORKSPACE}/Dockerfile \
		                  --destination=${DOCKER_USERNAME}/${APP_NAME}:latest
		              '''
		        }
		      }
		    }
		}
	    stage('Trigger commit pipe') {
		    agent any
		    environment{
		      def GIT_COMMIT = "${env.GIT_COMMIT}"
		    }
		    steps {
		    	script {
			    	echo "${env.GIT_COMMIT}"
				echo "triggering deployment"
				build job: 'commit', parameters: [string(name: 'DOCKERTAG', value: GIT_COMMIT)]
		    	}

		   }
	    }


        }
        post {
		always{
		    echo 'Package pipeline completed'
		}
	}
}

