void foo(char **value_to_return) {
  *value_to_return = malloc(256); // store 256 chars
  strcpy(*value_to_return, "deposited string");
}

int main() {
  char *deposit;
  foo(&deposit);
  printf("%s", deposit);
  return 257;
}