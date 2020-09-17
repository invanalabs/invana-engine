# invana-engine

GraphQL APIs for Apache TinkerPop supported graph databases.

**Note: Under active development.** 

[![Apache license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/invanalabs/invana-engine/blob/master/LICENSE) 
[![Build Status](https://travis-ci.org/invanalabs/invana-engine.svg?branch=develop)](https://travis-ci.org/invanalabs/invana-engine)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/invanalabs/invana-engine)](https://github.com/invanalabs/invana-engine/commits)
[![codecov](https://codecov.io/gh/invanalabs/invana-engine/branch/develop/graph/badge.svg)](https://codecov.io/gh/invanalabs/invana-engine)

## How to use

```
export GREMLIN_SERVER_URL="ws://localhost:8182/gremlin"
uvicorn invana.start_server:app --port 5000
```



## License 

Apache License 2.0
