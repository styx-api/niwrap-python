# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FILMBABE_METADATA = Metadata(
    id="99ed3b3c098c18b899137d170388e99e2fbc4432.boutiques",
    name="filmbabe",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FilmbabeParameters = typing.TypedDict('FilmbabeParameters', {
    "__STYXTYPE__": typing.Literal["filmbabe"],
    "datafile": InputPathType,
    "datafile_alias": InputPathType,
    "mask": InputPathType,
    "mask_alias": InputPathType,
    "designfile": InputPathType,
    "designfile_alias_1": InputPathType,
    "designfile_alias_2": InputPathType,
    "frf": InputPathType,
    "verbose_flag": bool,
    "verbose_flag_alias": bool,
    "debug_level": typing.NotRequired[str | None],
    "debug_level_alias_1": typing.NotRequired[str | None],
    "debug_level_alias_2": typing.NotRequired[str | None],
    "timing_on_flag": bool,
    "help_flag": bool,
    "help_flag_alias": bool,
    "flobs_prior_off_flag": bool,
    "flobs_prior_off_alias": bool,
    "flobs_dir": typing.NotRequired[str | None],
    "prior_covar_file": typing.NotRequired[InputPathType | None],
    "prior_covar_file_alias": typing.NotRequired[InputPathType | None],
    "prior_mean_file": typing.NotRequired[InputPathType | None],
    "prior_mean_file_alias": typing.NotRequired[InputPathType | None],
    "log_dir": typing.NotRequired[str | None],
    "log_dir_alias_1": typing.NotRequired[str | None],
    "log_dir_alias_2": typing.NotRequired[str | None],
    "num_iterations": typing.NotRequired[int | None],
    "temporal_ar_mrf_prec": typing.NotRequired[float | None],
    "temporal_ar_mrf_prec_alias": typing.NotRequired[float | None],
    "temporal_ar_flag": bool,
    "num_trace_samples": typing.NotRequired[int | None],
    "num_trace_samples_alias": typing.NotRequired[int | None],
    "temporal_ar_order": typing.NotRequired[int | None],
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
        "filmbabe": filmbabe_cargs,
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


class FilmbabeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `filmbabe(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def filmbabe_params(
    datafile: InputPathType,
    datafile_alias: InputPathType,
    mask: InputPathType,
    mask_alias: InputPathType,
    designfile: InputPathType,
    designfile_alias_1: InputPathType,
    designfile_alias_2: InputPathType,
    frf: InputPathType,
    verbose_flag: bool = False,
    verbose_flag_alias: bool = False,
    debug_level: str | None = None,
    debug_level_alias_1: str | None = None,
    debug_level_alias_2: str | None = None,
    timing_on_flag: bool = False,
    help_flag: bool = False,
    help_flag_alias: bool = False,
    flobs_prior_off_flag: bool = False,
    flobs_prior_off_alias: bool = False,
    flobs_dir: str | None = None,
    prior_covar_file: InputPathType | None = None,
    prior_covar_file_alias: InputPathType | None = None,
    prior_mean_file: InputPathType | None = None,
    prior_mean_file_alias: InputPathType | None = None,
    log_dir: str | None = None,
    log_dir_alias_1: str | None = None,
    log_dir_alias_2: str | None = None,
    num_iterations: int | None = 5,
    temporal_ar_mrf_prec: float | None = -1,
    temporal_ar_mrf_prec_alias: float | None = -1,
    temporal_ar_flag: bool = False,
    num_trace_samples: int | None = 0,
    num_trace_samples_alias: int | None = 0,
    temporal_ar_order: int | None = 3,
) -> FilmbabeParameters:
    """
    Build parameters.
    
    Args:
        datafile: Data file.
        datafile_alias: Data file.
        mask: Mask file.
        mask_alias: Mask file.
        designfile: Design matrix file.
        designfile_alias_1: Design matrix file.
        designfile_alias_2: Design matrix file.
        frf: File indicating which regressors belong to which original EV\
            design matrix file (a -1 label indicates a non-flobs regressor).
        verbose_flag: Switch on diagnostic messages.
        verbose_flag_alias: Switch on diagnostic messages.
        debug_level: Set debug level.
        debug_level_alias_1: Set debug level.
        debug_level_alias_2: Set debug level.
        timing_on_flag: Turn timing on.
        help_flag: Display help message.
        help_flag_alias: Display help message.
        flobs_prior_off_flag: Turn FLOBS prior off.
        flobs_prior_off_alias: Turn FLOBS prior off.
        flobs_dir: FLOBS directory; required when using FLOBS constraints.
        prior_covar_file: Prior covariance matrix file.
        prior_covar_file_alias: Prior covariance matrix file.
        prior_mean_file: Prior mean matrix file.
        prior_mean_file_alias: Prior mean matrix file.
        log_dir: Log directory.
        log_dir_alias_1: Log directory.
        log_dir_alias_2: Log directory.
        num_iterations: Number of VB iterations; default is 5.
        temporal_ar_mrf_prec: MRF precision to impose on temporal AR maps,\
            default is -1 for a proper full Bayes approach.
        temporal_ar_mrf_prec_alias: MRF precision to impose on temporal AR\
            maps, default is -1 for a proper full Bayes approach.
        temporal_ar_flag: Impose ARD/MRF on temporal AR.
        num_trace_samples: Number of samples to take to estimate trace; default\
            is 0 (uses only diagonal elements of precision matrix to estimate\
            trace).
        num_trace_samples_alias: Number of samples to take to estimate trace;\
            default is 0 (uses only diagonal elements of precision matrix to\
            estimate trace).
        temporal_ar_order: Order of temporal AR; default is 3.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "filmbabe",
        "datafile": datafile,
        "datafile_alias": datafile_alias,
        "mask": mask,
        "mask_alias": mask_alias,
        "designfile": designfile,
        "designfile_alias_1": designfile_alias_1,
        "designfile_alias_2": designfile_alias_2,
        "frf": frf,
        "verbose_flag": verbose_flag,
        "verbose_flag_alias": verbose_flag_alias,
        "timing_on_flag": timing_on_flag,
        "help_flag": help_flag,
        "help_flag_alias": help_flag_alias,
        "flobs_prior_off_flag": flobs_prior_off_flag,
        "flobs_prior_off_alias": flobs_prior_off_alias,
        "temporal_ar_flag": temporal_ar_flag,
    }
    if debug_level is not None:
        params["debug_level"] = debug_level
    if debug_level_alias_1 is not None:
        params["debug_level_alias_1"] = debug_level_alias_1
    if debug_level_alias_2 is not None:
        params["debug_level_alias_2"] = debug_level_alias_2
    if flobs_dir is not None:
        params["flobs_dir"] = flobs_dir
    if prior_covar_file is not None:
        params["prior_covar_file"] = prior_covar_file
    if prior_covar_file_alias is not None:
        params["prior_covar_file_alias"] = prior_covar_file_alias
    if prior_mean_file is not None:
        params["prior_mean_file"] = prior_mean_file
    if prior_mean_file_alias is not None:
        params["prior_mean_file_alias"] = prior_mean_file_alias
    if log_dir is not None:
        params["log_dir"] = log_dir
    if log_dir_alias_1 is not None:
        params["log_dir_alias_1"] = log_dir_alias_1
    if log_dir_alias_2 is not None:
        params["log_dir_alias_2"] = log_dir_alias_2
    if num_iterations is not None:
        params["num_iterations"] = num_iterations
    if temporal_ar_mrf_prec is not None:
        params["temporal_ar_mrf_prec"] = temporal_ar_mrf_prec
    if temporal_ar_mrf_prec_alias is not None:
        params["temporal_ar_mrf_prec_alias"] = temporal_ar_mrf_prec_alias
    if num_trace_samples is not None:
        params["num_trace_samples"] = num_trace_samples
    if num_trace_samples_alias is not None:
        params["num_trace_samples_alias"] = num_trace_samples_alias
    if temporal_ar_order is not None:
        params["temporal_ar_order"] = temporal_ar_order
    return params


def filmbabe_cargs(
    params: FilmbabeParameters,
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
    cargs.append("filmbabe")
    cargs.extend([
        "--df",
        execution.input_file(params.get("datafile"))
    ])
    cargs.extend([
        "--datafile",
        execution.input_file(params.get("datafile_alias"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask"))
    ])
    cargs.extend([
        "--mask",
        execution.input_file(params.get("mask_alias"))
    ])
    cargs.extend([
        "-d",
        execution.input_file(params.get("designfile"))
    ])
    cargs.extend([
        "--dm",
        execution.input_file(params.get("designfile_alias_1"))
    ])
    cargs.extend([
        "--designfile",
        execution.input_file(params.get("designfile_alias_2"))
    ])
    cargs.extend([
        "--frf",
        execution.input_file(params.get("frf"))
    ])
    if params.get("verbose_flag"):
        cargs.append("-V")
    if params.get("verbose_flag_alias"):
        cargs.append("--verbose")
    if params.get("debug_level") is not None:
        cargs.extend([
            "--db",
            params.get("debug_level")
        ])
    if params.get("debug_level_alias_1") is not None:
        cargs.extend([
            "--debug",
            params.get("debug_level_alias_1")
        ])
    if params.get("debug_level_alias_2") is not None:
        cargs.extend([
            "--debuglevel",
            params.get("debug_level_alias_2")
        ])
    if params.get("timing_on_flag"):
        cargs.append("--to")
    if params.get("help_flag"):
        cargs.append("-h")
    if params.get("help_flag_alias"):
        cargs.append("--help")
    if params.get("flobs_prior_off_flag"):
        cargs.append("--fpo")
    if params.get("flobs_prior_off_alias"):
        cargs.append("--flobsprioroff")
    if params.get("flobs_dir") is not None:
        cargs.extend([
            "--fd",
            params.get("flobs_dir")
        ])
    if params.get("prior_covar_file") is not None:
        cargs.extend([
            "--pcf",
            execution.input_file(params.get("prior_covar_file"))
        ])
    if params.get("prior_covar_file_alias") is not None:
        cargs.extend([
            "--priorcovarfile",
            execution.input_file(params.get("prior_covar_file_alias"))
        ])
    if params.get("prior_mean_file") is not None:
        cargs.extend([
            "--pmf",
            execution.input_file(params.get("prior_mean_file"))
        ])
    if params.get("prior_mean_file_alias") is not None:
        cargs.extend([
            "--priormeanfile",
            execution.input_file(params.get("prior_mean_file_alias"))
        ])
    if params.get("log_dir") is not None:
        cargs.extend([
            "-l",
            params.get("log_dir")
        ])
    if params.get("log_dir_alias_1") is not None:
        cargs.extend([
            "--ld",
            params.get("log_dir_alias_1")
        ])
    if params.get("log_dir_alias_2") is not None:
        cargs.extend([
            "--logdir",
            params.get("log_dir_alias_2")
        ])
    if params.get("num_iterations") is not None:
        cargs.extend([
            "--ni",
            str(params.get("num_iterations"))
        ])
    if params.get("temporal_ar_mrf_prec") is not None:
        cargs.extend([
            "--tmp",
            str(params.get("temporal_ar_mrf_prec"))
        ])
    if params.get("temporal_ar_mrf_prec_alias") is not None:
        cargs.extend([
            "--tarmrfprec",
            str(params.get("temporal_ar_mrf_prec_alias"))
        ])
    if params.get("temporal_ar_flag"):
        cargs.append("--tarard")
    if params.get("num_trace_samples") is not None:
        cargs.extend([
            "--nts",
            str(params.get("num_trace_samples"))
        ])
    if params.get("num_trace_samples_alias") is not None:
        cargs.extend([
            "--ntracesamps",
            str(params.get("num_trace_samples_alias"))
        ])
    if params.get("temporal_ar_order") is not None:
        cargs.extend([
            "--ntar",
            str(params.get("temporal_ar_order"))
        ])
    return cargs


def filmbabe_outputs(
    params: FilmbabeParameters,
    execution: Execution,
) -> FilmbabeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FilmbabeOutputs(
        root=execution.output_file("."),
    )
    return ret


def filmbabe_execute(
    params: FilmbabeParameters,
    execution: Execution,
) -> FilmbabeOutputs:
    """
    FILM with MCMC-based Bayesian Analysis for fMRI.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FilmbabeOutputs`).
    """
    params = execution.params(params)
    cargs = filmbabe_cargs(params, execution)
    ret = filmbabe_outputs(params, execution)
    execution.run(cargs)
    return ret


def filmbabe(
    datafile: InputPathType,
    datafile_alias: InputPathType,
    mask: InputPathType,
    mask_alias: InputPathType,
    designfile: InputPathType,
    designfile_alias_1: InputPathType,
    designfile_alias_2: InputPathType,
    frf: InputPathType,
    verbose_flag: bool = False,
    verbose_flag_alias: bool = False,
    debug_level: str | None = None,
    debug_level_alias_1: str | None = None,
    debug_level_alias_2: str | None = None,
    timing_on_flag: bool = False,
    help_flag: bool = False,
    help_flag_alias: bool = False,
    flobs_prior_off_flag: bool = False,
    flobs_prior_off_alias: bool = False,
    flobs_dir: str | None = None,
    prior_covar_file: InputPathType | None = None,
    prior_covar_file_alias: InputPathType | None = None,
    prior_mean_file: InputPathType | None = None,
    prior_mean_file_alias: InputPathType | None = None,
    log_dir: str | None = None,
    log_dir_alias_1: str | None = None,
    log_dir_alias_2: str | None = None,
    num_iterations: int | None = 5,
    temporal_ar_mrf_prec: float | None = -1,
    temporal_ar_mrf_prec_alias: float | None = -1,
    temporal_ar_flag: bool = False,
    num_trace_samples: int | None = 0,
    num_trace_samples_alias: int | None = 0,
    temporal_ar_order: int | None = 3,
    runner: Runner | None = None,
) -> FilmbabeOutputs:
    """
    FILM with MCMC-based Bayesian Analysis for fMRI.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        datafile: Data file.
        datafile_alias: Data file.
        mask: Mask file.
        mask_alias: Mask file.
        designfile: Design matrix file.
        designfile_alias_1: Design matrix file.
        designfile_alias_2: Design matrix file.
        frf: File indicating which regressors belong to which original EV\
            design matrix file (a -1 label indicates a non-flobs regressor).
        verbose_flag: Switch on diagnostic messages.
        verbose_flag_alias: Switch on diagnostic messages.
        debug_level: Set debug level.
        debug_level_alias_1: Set debug level.
        debug_level_alias_2: Set debug level.
        timing_on_flag: Turn timing on.
        help_flag: Display help message.
        help_flag_alias: Display help message.
        flobs_prior_off_flag: Turn FLOBS prior off.
        flobs_prior_off_alias: Turn FLOBS prior off.
        flobs_dir: FLOBS directory; required when using FLOBS constraints.
        prior_covar_file: Prior covariance matrix file.
        prior_covar_file_alias: Prior covariance matrix file.
        prior_mean_file: Prior mean matrix file.
        prior_mean_file_alias: Prior mean matrix file.
        log_dir: Log directory.
        log_dir_alias_1: Log directory.
        log_dir_alias_2: Log directory.
        num_iterations: Number of VB iterations; default is 5.
        temporal_ar_mrf_prec: MRF precision to impose on temporal AR maps,\
            default is -1 for a proper full Bayes approach.
        temporal_ar_mrf_prec_alias: MRF precision to impose on temporal AR\
            maps, default is -1 for a proper full Bayes approach.
        temporal_ar_flag: Impose ARD/MRF on temporal AR.
        num_trace_samples: Number of samples to take to estimate trace; default\
            is 0 (uses only diagonal elements of precision matrix to estimate\
            trace).
        num_trace_samples_alias: Number of samples to take to estimate trace;\
            default is 0 (uses only diagonal elements of precision matrix to\
            estimate trace).
        temporal_ar_order: Order of temporal AR; default is 3.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FilmbabeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILMBABE_METADATA)
    params = filmbabe_params(
        datafile=datafile,
        datafile_alias=datafile_alias,
        mask=mask,
        mask_alias=mask_alias,
        designfile=designfile,
        designfile_alias_1=designfile_alias_1,
        designfile_alias_2=designfile_alias_2,
        frf=frf,
        verbose_flag=verbose_flag,
        verbose_flag_alias=verbose_flag_alias,
        debug_level=debug_level,
        debug_level_alias_1=debug_level_alias_1,
        debug_level_alias_2=debug_level_alias_2,
        timing_on_flag=timing_on_flag,
        help_flag=help_flag,
        help_flag_alias=help_flag_alias,
        flobs_prior_off_flag=flobs_prior_off_flag,
        flobs_prior_off_alias=flobs_prior_off_alias,
        flobs_dir=flobs_dir,
        prior_covar_file=prior_covar_file,
        prior_covar_file_alias=prior_covar_file_alias,
        prior_mean_file=prior_mean_file,
        prior_mean_file_alias=prior_mean_file_alias,
        log_dir=log_dir,
        log_dir_alias_1=log_dir_alias_1,
        log_dir_alias_2=log_dir_alias_2,
        num_iterations=num_iterations,
        temporal_ar_mrf_prec=temporal_ar_mrf_prec,
        temporal_ar_mrf_prec_alias=temporal_ar_mrf_prec_alias,
        temporal_ar_flag=temporal_ar_flag,
        num_trace_samples=num_trace_samples,
        num_trace_samples_alias=num_trace_samples_alias,
        temporal_ar_order=temporal_ar_order,
    )
    return filmbabe_execute(params, execution)


__all__ = [
    "FILMBABE_METADATA",
    "FilmbabeOutputs",
    "FilmbabeParameters",
    "filmbabe",
    "filmbabe_params",
]
