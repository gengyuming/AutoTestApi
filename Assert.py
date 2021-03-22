import threading


class Assert:
    # 期待值等于实际值
    @staticmethod
    def is_equal(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if str(expected_value) != str(actual_value):
            if position is not None:
                result_detail += position
            else:
                result_detail += '\nExpected value and Actual value are not equal'

            print(1)
            result = False
        else:
            print(2)
            result = True

        print(result_detail)

        return result

    # 期待值不等于实际值
    @staticmethod
    def is_not_equal(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if str(expected_value) == str(actual_value):
            if position is not None:
                result_detail += position
            else:
                result_detail += '\nExpected value and Actual value are equal'

            print(1)
        else:
            print(2)

        print(result_detail)

    # 期待值包含实际值
    @staticmethod
    def is_containing(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if type(actual_value) is list:
            if expected_value not in actual_value:
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected list values are not in Actual values.'

                print(1)
            else:
                print(2)

            print(result_detail)
        else:
            if not str(actual_value).__contains__(str(expected_value)):
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected string value is not in Actual string value.'

                print(1)
            else:
                print(2)

            print(result_detail)

    # 期待值不包含实际值
    @staticmethod
    def is_not_containing(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if type(actual_value) is list:
            if expected_value in actual_value:
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected list values are in Actual list values.'

                print(1)
            else:
                print(2)

            print(result_detail)
        else:
            if str(actual_value).__contains__(str(expected_value)):
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected string value is in Actual string value.'

                print(1)
            else:
                print(2)

            print(result_detail)

    # 期待值大于实际值
    @staticmethod
    def is_greater_than(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(expected_value, actual_value)

        if expected_value < actual_value:
            if position is not None:
                result_detail += position
            else:
                result_detail += '\nExpected value is not greater then Actual value'

            print(1)
        else:
            print(2)

        print(result_detail)

    # 期待值小于实际值
    @staticmethod
    def is_less_than(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(expected_value, actual_value)

        if expected_value > actual_value:
            if position is not None:
                result_detail += str(position)
            else:
                result_detail += '\nExpected value is not less then Actual value'

            print(1)
        else:
            print(2)

        print(result_detail)


