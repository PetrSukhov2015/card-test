def before_scenario(context, feature):
    # now = datetime.datetime.now()
    # the_file_name_pattern = os.path.basename(__file__)[:-3] + "___result____" + now.strftime("%Y-%m-%d___%H%M%S")
    # context.rg2 = Report(the_file_name_pattern, context.driver)
    print('It is before scenario')

def after_scenario(context, feature):
    # context.rg2.make_report(context.join_result)
    print('after scenario')
