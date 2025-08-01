# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TEST_TUTORIALS_SH_METADATA = Metadata(
    id="9883254460c717895085469ee6ef3030faa9e4a9.boutiques",
    name="test_tutorials.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TestTutorialsShParameters = typing.TypedDict('TestTutorialsShParameters', {
    "__STYXTYPE__": typing.Literal["test_tutorials.sh"],
    "all_tutorials": bool,
    "quick_test": bool,
    "auto_quit_freeview": bool,
    "skip_all_guis": bool,
    "skip_tk_guis": bool,
    "skip_qdec_guis": bool,
    "individual_subject": bool,
    "troubleshooting": bool,
    "group_analysis": bool,
    "qdec": bool,
    "longitudinal": bool,
    "roi_analysis": bool,
    "diffusion": bool,
    "tracula": bool,
    "fsfast": bool,
    "multimodal": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "test_tutorials.sh": test_tutorials_sh_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class TestTutorialsShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `test_tutorials_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def test_tutorials_sh_params(
    all_tutorials: bool = False,
    quick_test: bool = False,
    auto_quit_freeview: bool = False,
    skip_all_guis: bool = False,
    skip_tk_guis: bool = False,
    skip_qdec_guis: bool = False,
    individual_subject: bool = False,
    troubleshooting: bool = False,
    group_analysis: bool = False,
    qdec: bool = False,
    longitudinal: bool = False,
    roi_analysis: bool = False,
    diffusion: bool = False,
    tracula: bool = False,
    fsfast: bool = False,
    multimodal: bool = False,
) -> TestTutorialsShParameters:
    """
    Build parameters.
    
    Args:
        all_tutorials: Run all tutorials.
        quick_test: Perform a quick subset of commands.
        auto_quit_freeview: Automatically closes freeview after opening.
        skip_all_guis: Skips all commands that open a GUI.
        skip_tk_guis: Skips commands that open a tk GUI (tkmedit, tksurfer,\
            etc).
        skip_qdec_guis: Skips commands that open qdec.
        individual_subject: Do Interaction with Individual Subject Data\
            tutorial.
        troubleshooting: Do Troubleshooting tutorial.
        group_analysis: Do Group Analysis tutorial.
        qdec: Do QDEC tutorial.
        longitudinal: Do Longitudinal tutorial.
        roi_analysis: Do ROI Analysis tutorial.
        diffusion: Do Diffusion tutorial.
        tracula: Do TRACULA tutorial.
        fsfast: Do FSFASt tutorial.
        multimodal: Do Mulimodal tutorial.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "test_tutorials.sh",
        "all_tutorials": all_tutorials,
        "quick_test": quick_test,
        "auto_quit_freeview": auto_quit_freeview,
        "skip_all_guis": skip_all_guis,
        "skip_tk_guis": skip_tk_guis,
        "skip_qdec_guis": skip_qdec_guis,
        "individual_subject": individual_subject,
        "troubleshooting": troubleshooting,
        "group_analysis": group_analysis,
        "qdec": qdec,
        "longitudinal": longitudinal,
        "roi_analysis": roi_analysis,
        "diffusion": diffusion,
        "tracula": tracula,
        "fsfast": fsfast,
        "multimodal": multimodal,
    }
    return params


def test_tutorials_sh_cargs(
    params: TestTutorialsShParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("test_tutorials.sh")
    if params.get("all_tutorials"):
        cargs.append("-all")
    if params.get("quick_test"):
        cargs.append("-quick")
    if params.get("auto_quit_freeview"):
        cargs.append("-auto_quit_freeview")
    if params.get("skip_all_guis"):
        cargs.append("-skip_all_guis")
    if params.get("skip_tk_guis"):
        cargs.append("-skip_tk_guis")
    if params.get("skip_qdec_guis"):
        cargs.append("-skip_qdec_guis")
    if params.get("individual_subject"):
        cargs.append("-individual_subject")
    if params.get("troubleshooting"):
        cargs.append("-troubleshooting")
    if params.get("group_analysis"):
        cargs.append("-group_analysis")
    if params.get("qdec"):
        cargs.append("-qdec")
    if params.get("longitudinal"):
        cargs.append("-longitudinal")
    if params.get("roi_analysis"):
        cargs.append("-roi_analysis")
    if params.get("diffusion"):
        cargs.append("-diffusion")
    if params.get("tracula"):
        cargs.append("-tracula")
    if params.get("fsfast"):
        cargs.append("-fsfast")
    if params.get("multimodal"):
        cargs.append("-multimodal")
    return cargs


def test_tutorials_sh_outputs(
    params: TestTutorialsShParameters,
    execution: Execution,
) -> TestTutorialsShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TestTutorialsShOutputs(
        root=execution.output_file("."),
    )
    return ret


def test_tutorials_sh_execute(
    params: TestTutorialsShParameters,
    execution: Execution,
) -> TestTutorialsShOutputs:
    """
    A script to run various tutorial commands, with options for skipping GUI
    components and focusing on specific tutorials.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TestTutorialsShOutputs`).
    """
    params = execution.params(params)
    cargs = test_tutorials_sh_cargs(params, execution)
    ret = test_tutorials_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def test_tutorials_sh(
    all_tutorials: bool = False,
    quick_test: bool = False,
    auto_quit_freeview: bool = False,
    skip_all_guis: bool = False,
    skip_tk_guis: bool = False,
    skip_qdec_guis: bool = False,
    individual_subject: bool = False,
    troubleshooting: bool = False,
    group_analysis: bool = False,
    qdec: bool = False,
    longitudinal: bool = False,
    roi_analysis: bool = False,
    diffusion: bool = False,
    tracula: bool = False,
    fsfast: bool = False,
    multimodal: bool = False,
    runner: Runner | None = None,
) -> TestTutorialsShOutputs:
    """
    A script to run various tutorial commands, with options for skipping GUI
    components and focusing on specific tutorials.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        all_tutorials: Run all tutorials.
        quick_test: Perform a quick subset of commands.
        auto_quit_freeview: Automatically closes freeview after opening.
        skip_all_guis: Skips all commands that open a GUI.
        skip_tk_guis: Skips commands that open a tk GUI (tkmedit, tksurfer,\
            etc).
        skip_qdec_guis: Skips commands that open qdec.
        individual_subject: Do Interaction with Individual Subject Data\
            tutorial.
        troubleshooting: Do Troubleshooting tutorial.
        group_analysis: Do Group Analysis tutorial.
        qdec: Do QDEC tutorial.
        longitudinal: Do Longitudinal tutorial.
        roi_analysis: Do ROI Analysis tutorial.
        diffusion: Do Diffusion tutorial.
        tracula: Do TRACULA tutorial.
        fsfast: Do FSFASt tutorial.
        multimodal: Do Mulimodal tutorial.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TestTutorialsShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEST_TUTORIALS_SH_METADATA)
    params = test_tutorials_sh_params(
        all_tutorials=all_tutorials,
        quick_test=quick_test,
        auto_quit_freeview=auto_quit_freeview,
        skip_all_guis=skip_all_guis,
        skip_tk_guis=skip_tk_guis,
        skip_qdec_guis=skip_qdec_guis,
        individual_subject=individual_subject,
        troubleshooting=troubleshooting,
        group_analysis=group_analysis,
        qdec=qdec,
        longitudinal=longitudinal,
        roi_analysis=roi_analysis,
        diffusion=diffusion,
        tracula=tracula,
        fsfast=fsfast,
        multimodal=multimodal,
    )
    return test_tutorials_sh_execute(params, execution)


__all__ = [
    "TEST_TUTORIALS_SH_METADATA",
    "TestTutorialsShOutputs",
    "TestTutorialsShParameters",
    "test_tutorials_sh",
    "test_tutorials_sh_params",
]
