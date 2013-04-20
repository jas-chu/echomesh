#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>

#include "ReadThread.h"
#include "LightComponent.h"
#include "LineGetter.h"

namespace echomesh {

using namespace std;

static const char READ_FILE[] = "/development/echomesh/incoming.data";

ReadThread::ReadThread(const String& commandLine)
    : Thread("ReadThread"),
      lineGetter_(makeLineGetter(commandLine)) {
}

ReadThread::~ReadThread() {}

void ReadThread::run() {
  string s;
  while (!lineGetter_->eof()) {
    try {
      log("starting to getline");
      s = lineGetter_->getLine();
      log("gotline " + s);
    } catch (Exception e) {
      log("ERROR: " + e.what_str());
      break;
    }
    log2("!!!" + s);
    if (s.find("---")) {
      accum_.add(s.c_str());
    } else {
      String result = accum_.joinIntoString("\n");
      accum_.clear();
      handleMessage(string(result.toUTF8()));
    }
  }
  log("eof!");
  quit();
}

namespace {

CriticalSection lock_;

const char FILENAME[] = "/tmp/echomesh.log";
OutputStream* STREAM = NULL;

const char FILENAME2[] = "/tmp/echomesh.2.log";
OutputStream* STREAM2 = NULL;

}  // namespace

void log(const string& msg) {
  if (!*FILENAME)
    return;
  ScopedLock l(lock_);
  if (!STREAM) {
    File f(FILENAME);
    f.deleteFile();
    STREAM = new FileOutputStream(f);
  }
  STREAM->write(msg.data(), msg.size());
  STREAM->write("\n", 1);
  STREAM->flush();
}

void log2(const string& msg) {
  if (!*FILENAME2)
    return;
  ScopedLock l(lock_);
  if (!STREAM2) {
    File f(FILENAME2);
    f.deleteFile();
    STREAM2 = new FileOutputStream(f);
  }
  STREAM2->write(msg.data(), msg.size());
  // STREAM2->write("\n", 1);
  STREAM2->flush();
}


void close_log() {
  delete STREAM;
  STREAM = NULL;

  delete STREAM2;
  STREAM2 = NULL;
}

}  // namespace echomesh