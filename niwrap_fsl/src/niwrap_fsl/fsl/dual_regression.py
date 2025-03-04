# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DUAL_REGRESSION_METADATA = Metadata(
    id="4ca133e6806abb8249af8771d3f5b7613b9bab63.boutiques",
    name="dual_regression",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


DualRegressionParameters = typing.TypedDict('DualRegressionParameters', {
    "__STYX_TYPE__": typing.Literal["dual_regression"],
    "group_ic_maps": InputPathType,
    "des_norm": float,
    "design_mat": InputPathType,
    "design_con": InputPathType,
    "n_perm": float,
    "thr_flag": bool,
    "output_directory": str,
    "input_files": list[InputPathType],
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
        "dual_regression": dual_regression_cargs,
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
        "dual_regression": dual_regression_outputs,
    }.get(t)


class DualRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dual_regression(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stage1_output: OutputPathType
    """Output from stage 1 for each subject"""
    stage2_output: OutputPathType
    """Output from stage 2 for each subject"""
    stage3_output: OutputPathType
    """Output from stage 3 for each subject"""
    randomise_output: OutputPathType
    """Output of randomise"""


def dual_regression_params(
    group_ic_maps: InputPathType,
    des_norm: float,
    design_mat: InputPathType,
    design_con: InputPathType,
    n_perm: float,
    output_directory: str,
    input_files: list[InputPathType],
    thr_flag: bool = False,
) -> DualRegressionParameters:
    """
    Build parameters.
    
    Args:
        group_ic_maps: 4D image containing spatial IC maps (melodic_IC) from\
            the whole-group ICA analysis.
        des_norm: 0 or 1 (1 is recommended). Whether to variance-normalise the\
            timecourses used as the stage-2 regressors.
        design_mat: Design matrix for final cross-subject modelling with\
            randomise.
        design_con: Design contrasts for final cross-subject modelling with\
            randomise.
        n_perm: Number of permutations for randomise; set to 1 for just raw\
            tstat output, set to 0 to not run randomise at all.
        output_directory: This directory will be created to hold all output and\
            logfiles.
        input_files: List of all subjects' preprocessed, standard-space 4D\
            datasets.
        thr_flag: Perform thresholded dual regression to obtain unbiased\
            timeseries for connectomics analyses (e.g., with FSLnets).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dual_regression",
        "group_ic_maps": group_ic_maps,
        "des_norm": des_norm,
        "design_mat": design_mat,
        "design_con": design_con,
        "n_perm": n_perm,
        "thr_flag": thr_flag,
        "output_directory": output_directory,
        "input_files": input_files,
    }
    return params


def dual_regression_cargs(
    params: DualRegressionParameters,
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
    cargs.append("dual_regression")
    cargs.append(execution.input_file(params.get("group_ic_maps")))
    cargs.append(str(params.get("des_norm")))
    cargs.append(execution.input_file(params.get("design_mat")))
    cargs.append(execution.input_file(params.get("design_con")))
    cargs.append(str(params.get("n_perm")))
    if params.get("thr_flag"):
        cargs.append("--thr")
    cargs.append(params.get("output_directory"))
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def dual_regression_outputs(
    params: DualRegressionParameters,
    execution: Execution,
) -> DualRegressionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DualRegressionOutputs(
        root=execution.output_file("."),
        stage1_output=execution.output_file(params.get("output_directory") + "/dr_stage1_subject[SUBJECT_INDEX].nii.gz"),
        stage2_output=execution.output_file(params.get("output_directory") + "/dr_stage2_subject[SUBJECT_INDEX].nii.gz"),
        stage3_output=execution.output_file(params.get("output_directory") + "/dr_stage3_subject[SUBJECT_INDEX].nii.gz"),
        randomise_output=execution.output_file(params.get("output_directory") + "/dr_randomise"),
    )
    return ret


def dual_regression_execute(
    params: DualRegressionParameters,
    execution: Execution,
) -> DualRegressionOutputs:
    """
    Dual regression algorithm to investigate group-ICA results.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DualRegressionOutputs`).
    """
    params = execution.params(params)
    cargs = dual_regression_cargs(params, execution)
    ret = dual_regression_outputs(params, execution)
    execution.run(cargs)
    return ret


def dual_regression(
    group_ic_maps: InputPathType,
    des_norm: float,
    design_mat: InputPathType,
    design_con: InputPathType,
    n_perm: float,
    output_directory: str,
    input_files: list[InputPathType],
    thr_flag: bool = False,
    runner: Runner | None = None,
) -> DualRegressionOutputs:
    """
    Dual regression algorithm to investigate group-ICA results.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        group_ic_maps: 4D image containing spatial IC maps (melodic_IC) from\
            the whole-group ICA analysis.
        des_norm: 0 or 1 (1 is recommended). Whether to variance-normalise the\
            timecourses used as the stage-2 regressors.
        design_mat: Design matrix for final cross-subject modelling with\
            randomise.
        design_con: Design contrasts for final cross-subject modelling with\
            randomise.
        n_perm: Number of permutations for randomise; set to 1 for just raw\
            tstat output, set to 0 to not run randomise at all.
        output_directory: This directory will be created to hold all output and\
            logfiles.
        input_files: List of all subjects' preprocessed, standard-space 4D\
            datasets.
        thr_flag: Perform thresholded dual regression to obtain unbiased\
            timeseries for connectomics analyses (e.g., with FSLnets).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DualRegressionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DUAL_REGRESSION_METADATA)
    params = dual_regression_params(
        group_ic_maps=group_ic_maps,
        des_norm=des_norm,
        design_mat=design_mat,
        design_con=design_con,
        n_perm=n_perm,
        thr_flag=thr_flag,
        output_directory=output_directory,
        input_files=input_files,
    )
    return dual_regression_execute(params, execution)


__all__ = [
    "DUAL_REGRESSION_METADATA",
    "DualRegressionOutputs",
    "DualRegressionParameters",
    "dual_regression",
    "dual_regression_params",
]
