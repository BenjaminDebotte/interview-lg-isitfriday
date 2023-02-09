pipeline {
  environment {
      CI=true
  }
  options {
    timestamps()
    ansiColor('xterm')
  }
  stages {
    stage('Run pre-commit') {
      steps {
        sh 'set'
        sh 'pre-commit run --all'
      }
    }

    stage('Build Docker') {
      when {
        anyOf {
            tag "*.*.*"
            branch "master"
        }
      }

      stage('Build & Publish {
        steps {
          sh 'set'
          sh 'docker build -t it-is-friday:${BRANCH_NAME} --rm --build-arg http_proxy="${http_proxy}" --build-arg no_proxy="${no_proxy}" .'
          sh 'docker tag it-is-friday:${BRANCH_NAME} ${DOCKER_REGISTRY}/it-is-friday:${BRANCH_NAME}'
          sh 'docker push ${DOCKER_REGISTRY}/it-is-friday:${BRANCH_NAME}'
        }
      }
    }

  }
}
